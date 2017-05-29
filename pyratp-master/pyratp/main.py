# -*- coding: utf-8 -*-
__author__ = 'paronax'
import os
import urllib3
from .exceptions import InvalidFacetError, InvalidLanguageError

_pyrapt_verbosity_mode = False
_pyrapt_domain = "http://data.ratp.fr"
_pyrapt_datasets = _pyrapt_domain + "/api/datasets/1.0/search/"
_pyrapt_dataset_search = _pyrapt_domain + "/api/datasets/1.0/{}/"
_pyrapt_records_stream = _pyrapt_domain + "/api/records/1.0/search/"
_pyrapt_records_dl = _pyrapt_domain + "/api/records/1.0/download/"

_pyrapt_facets = ['modified', 'publisher', 'issued',
                          'accrualperiodicity', 'language', 'license',
                          'granularity', 'dataquality', 'theme', 'keyword',
                          'created', 'creator', 'contributor']
_pyrapt_sorts = ['modified', 'issued', 'created']


# So-called 'public' methods
def set_pyrapt_dir(data_dir=os.getcwd()):
    _pyrapt_data_dir = data_dir

def get_datasets_list():
    try:
        http = urllib3.PoolManager()
        req = http.request('GET', _pyrapt_datasets)
        return req.read()
    except:
        print("Cela n'a pas de sens")
        raise
    finally:
        http.clear()


def browse_dataset(lang='fr', facets='', refines='', excludes='', sort='',
                   rows=10, start=0, pretty_print=False):
    #TODO what if multiple facets ?
    try:
        params = {'lang':  lang,
                  'facet[]': facets,
                  'refines[]': refines,
                  'excludes[]': excludes,
                  'sort': sort,
                  'rows': rows,
                  'start': start,
                  'pretty_print': pretty_print
                }
        http = urllib3.PoolManager()
        req = http.request('GET', _pyrapt_datasets, params)


    except InvalidFacetError as e:
        print("It does not work : " + e.message)
    except InvalidLanguageError as e:
        print("It does not work : " + e.message)
    except urllib3.exceptions.HTTPError as e:
        print("it does not work ! " + str(e))
    except:
        print("Unexpected error")
        raise
    else:
        print("it works !")
    finally:
        http.clear()


def get_dataset(datasetid, pretty_print=False):
    data_format='JSON'
    print("coucou")


# Return whether records or downloaded filelists
def get_records():
    print("coucou")


def download_dataset():
    print("coucou")


# So-called 'private' methods

def _verify_facet(facet):
    if facet not in _pyrapt_facets:
        raise InvalidFacetError(facet)
