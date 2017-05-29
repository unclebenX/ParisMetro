# -*- coding: utf-8 -*-
__author__ = 'paronax'

class InvalidFacetError(ValueError):
    def __init__(self, message):
        self.message = 'Unknown facet : ' + message


class InvalidLanguageError(ValueError):
    def __init__(self, message):
        self.message = 'Unknown language : ' + message