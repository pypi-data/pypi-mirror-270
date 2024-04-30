import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Package dependencies
install_requires = [
    'requests',
]

# Testing dependencies
testing_extras = [
    'pytest',
    'pytest-env',
    'coverage',
    'pytest-cov',
]

# Documentation dependencies
documentation_extras = [
    'sphinx',
]

setup(
    name='gagnatorg',
    version='0.1.0',
    packages=['gagnatorg'],
    include_package_data=True,
    license='MIT',
    description='Python package to interact with the Já Gagnatorg API.',
    long_description=README,
    url='https://github.com/overcastsoftware/gagnatorg-python/',
    author='Overcast',
    author_email='hallo@overcast.is',
    long_description_content_type="text/markdown",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)