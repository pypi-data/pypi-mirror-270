 # -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
import base64
from .errors import GagnatorgException, GagnatorgNotFoundException
import uuid
from enum import Enum
import requests



class GagnatorgClient(object):

    def __init__(self, apikey):
        self.APIKEY = apikey
        self.ENDPOINT = 'https://api.ja.is/skra/v1/'

    def make_request(self, action, method, **args):
        headers = {
            'Authorization': self.APIKEY,
        }
        if method == 'GET':
            response = requests.get(self.format_url(action), headers=headers, **args)
        if method == 'POST':
            response = requests.post(self.format_url(action), headers=headers, **args)

        self.check_error(response)
        return response.json()

    def format_url(self, path):
        return "{}{}".format(self.ENDPOINT, path)

    def check_error(self, response):
        if response.status_code == 400:
            error = response.json()
            output = f"{error['type']}: {error['error']}"
            raise GagnatorgException(output)
        if response.status_code == 404:
            error = response.json()
            output = f"{error['type']}: {error['error']}"
            raise GagnatorgNotFoundException(output)
        if response.status_code == 401:
            raise GagnatorgException("401 credentials error")
        if response.status_code == 500:
            raise GagnatorgException("500 server error")

    def clean_kennitala(self, kennitala):
        kennitala = kennitala.replace('-', '')
        kennitala = kennitala.replace(' ', '')

        return kennitala

    def GetKennitolur(self, kennitala):
        kennitala = self.clean_kennitala(kennitala)
        return self.make_request(f'kennitolur/{kennitala}', 'GET')
    
    def GetPeople(self, kennitala):
        kennitala = self.clean_kennitala(kennitala)
        return self.make_request(f'people/{kennitala}', 'GET')
    
    def GetBusinesses(self, kennitala):
        kennitala = self.clean_kennitala(kennitala)
        return self.make_request(f'businesses/{kennitala}', 'GET')
    
    def GetPostalCodes(self, postal_code=None):
        if postal_code:
            return self.make_request(f'postal-codes/{postal_code}', 'GET')
        return self.make_request(f'postal-codes', 'GET')

    # class SubsequentTransactionTypes(Enum):

    #     CardholderInitiatedCredentialOnFile = 'CardholderInitiatedCredentialOnFile'
    #     MerchantInitiatedCredentialOnFile = 'MerchantInitiatedCredentialOnFile'
    #     MerchantInitiatedRecurring = 'MerchantInitiatedRecurring'
    #     MerchantInitiatedInstallment = 'MerchantInitiatedInstallment'
    #     MerchantInitiatedIncremental = 'MerchantInitiatedIncremental'
    #     MerchantInitiatedResubmission = 'MerchantInitiatedResubmission'
    #     MerchantInitiatedDelayedCharges = 'MerchantInitiatedDelayedCharges'
    #     MerchantInitiatedReauthorization = 'MerchantInitiatedReauthorization'
    #     MerchantInitiatedNoShow = 'MerchantInitiatedNoShow'
