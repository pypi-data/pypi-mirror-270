# -*- coding: utf-8 -*-

import os

from .context import gagnatorg

import unittest
import pytest
from random import randint



@pytest.fixture
def credentials():
    apikey = os.getenv('GAGNATORG_APIKEY', None)
    
    return {
        'apikey': apikey,
    }

@pytest.fixture
def wrong_credentials():
    return {
        'apikey': "DummyApiKey"
    }

@pytest.fixture
def gagnatorg_client(credentials):
    return gagnatorg.GagnatorgClient(**credentials)

@pytest.fixture
def wrong_gagnatorg_client(wrong_credentials):
    return gagnatorg.GagnatorgClient(**wrong_credentials)

def test_can_init_client(credentials):
    gagnatorg_client = gagnatorg.GagnatorgClient(**credentials)

@pytest.mark.valitorpay
def test_lookup_without_credentials_raises_exception(wrong_gagnatorg_client):

    with pytest.raises(gagnatorg.GagnatorgException) as exc_info:
        response = wrong_gagnatorg_client.GetPeople('0308833819')

def test_validate_kennitala(gagnatorg_client):
    response = gagnatorg_client.GetKennitolur('4308050530')
    assert response['valid'] == True

def test_validate_kennitala_fails(gagnatorg_client):
    response = gagnatorg_client.GetKennitolur('1111111111')
    assert response['valid'] == False

def test_people_lookup_not_found_raises_exception(gagnatorg_client):
    with pytest.raises(gagnatorg.GagnatorgNotFoundException) as exc_info:
        response = gagnatorg_client.GetPeople('0102034579')

    assert exc_info.value.message == 'error: no person with kennitala 0102034579'

def test_people_lookup_finds_person(gagnatorg_client):
    response = gagnatorg_client.GetPeople('0308833819')
    print(response)
    assert response['name'] == 'Sævar Öfjörð Magnússon'

def test_people_lookup_with_hyphen_finds_person(gagnatorg_client):
    response = gagnatorg_client.GetPeople('030883-3819')
    assert response['name'] == 'Sævar Öfjörð Magnússon'

def test_people_lookup_with_space_finds_person(gagnatorg_client):
    response = gagnatorg_client.GetPeople('030883 3819')
    assert response['name'] == 'Sævar Öfjörð Magnússon'

def test_people_lookup_with_lspace_finds_person(gagnatorg_client):
    response = gagnatorg_client.GetPeople(' 0308833819')
    assert response['name'] == 'Sævar Öfjörð Magnússon'

def test_people_lookup_with_rspace_finds_person(gagnatorg_client):
    response = gagnatorg_client.GetPeople('0308833819 ')
    assert response['name'] == 'Sævar Öfjörð Magnússon'

def test_people_lookup_with_company_kennitala_raises_exception(gagnatorg_client):
    with pytest.raises(gagnatorg.GagnatorgNotFoundException) as exc_info:
        response = gagnatorg_client.GetPeople('5104130670')
    assert exc_info.value.message == 'error: no person with kennitala 5104130670'
    
def test_business_lookup_finds_business(gagnatorg_client):
    response = gagnatorg_client.GetBusinesses('5104130670')
    assert response['full_name'] == 'Overcast ehf.'

def test_business_lookup_with_hyphen_finds_business(gagnatorg_client):
    response = gagnatorg_client.GetBusinesses('510413-0670')
    assert response['full_name'] == 'Overcast ehf.'

def test_business_lookup_with_space_finds_business(gagnatorg_client):
    response = gagnatorg_client.GetBusinesses('510413 0670')
    assert response['full_name'] == 'Overcast ehf.'

def test_postal_code_get_finds_all_postal_codes(gagnatorg_client):
    response = gagnatorg_client.GetPostalCodes()
    assert len(response['items']) > 0

def test_postal_code_get_single(gagnatorg_client):
    response = gagnatorg_client.GetPostalCodes('101')
    assert list(response.keys()) == ['type', 'postal_code', 'town']