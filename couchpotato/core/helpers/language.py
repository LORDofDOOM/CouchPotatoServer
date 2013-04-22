'''
Created on 11.11.2012

@author: adlerre
'''
from couchpotato.environment import Env

languageCodes = {
                'de': {'long' : 'de-DE', 'search' :'german'},
                'en': {'long' : 'en-US', 'search' :''},
                'cs': {'long' : 'en-US', 'search' :'Czech'},
                'da': {'long' : 'en-US', 'search' :'Danish'},
                'es': {'long' : 'en-US', 'search' :'Spanish'},
                'fi': {'long' : 'en-US', 'search' :'Finnish'},
                'fr': {'long' : 'en-US', 'search' :'French'},
                'he': {'long' : 'en-US', 'search' :'Hebrew'},
                'it': {'long' : 'en-US', 'search' :'Italian'},
                'nl': {'long' : 'en-US', 'search' :'Dutch'},
                'pl': {'long' : 'en-US', 'search' :'Polish'},
                'pt': {'long' : 'en-US', 'search' :'Portuguese'},
                'ru': {'long' : 'en-US', 'search' :'Russian'},
                'sv': {'long' : 'en-US', 'search' :'Swedish'},
                'tr': {'long' : 'en-US', 'search' :'Turkish'},
                'uk': {'long' : 'en-US', 'search' :'Ukrainian'},
                'zh': {'long' : 'en-US', 'search' :'Chinese'}
                }

def defaultLang():
    return Env.setting('language', 'searcher', None, "de")

def langCodeLong(lang="de"):
    return languageCodes[lang]['long']

def langSearch(lang="de"):
    return languageCodes[lang]['search']
