from setuptools import setup

setup(
    name='cardpydentity',
    version='0.2.0',
    install_requires=[
        'requests',
        'fuzzywuzzy',
        'python-Levenshtein',
        'appdirs'
    ],
)