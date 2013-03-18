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
    return Env.setting('language', 'searcher', None, "en")

def langCodeLong(lang="en"):
    return languageCodes[lang]['long']

def langSearch(lang="en"):
    return languageCodes[lang]['search']
