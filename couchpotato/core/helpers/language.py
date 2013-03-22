'''
Created on 11.11.2012

@author: adlerre
'''
from couchpotato.environment import Env

languageCodes = {
                 'de': {'long' : 'de-DE', 'search' :'german'},
                 'en': {'long' : 'en-US', 'search' :''}
                }

def defaultLang():
    return Env.setting('language', 'searcher', None, "de")

def langCodeLong(lang="de"):
    return languageCodes[lang]['long']

def langSearch(lang="de"):
    return languageCodes[lang]['search']
