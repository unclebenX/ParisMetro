# -*- coding: utf-8 -*-
__author__ = 'paronax'

#TODO do modelisation
class DataSet():
    def __init__(self, datasetid, metas, has_records, features, attachments,
                       fields):
        self.datasetid = datasetid
        self.metas = metas
        self.has_records = has_records
        self.features = features
        self.attachments = attachments
        self.fiels = fields
        self.records = []


