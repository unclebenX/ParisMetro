# -*- coding: utf-8 -*-
__author__ = 'paronax'

import unittest
import pyratp.main

class MyTestCase1(unittest.TestCase):
    def setUp(self):
        print("coucou")

    def test_isgood(self):
        req = pyratp.main.get_datasets_list()
        print(req)
        self.assertEqual(req is not None, True)

    def tearDown(self):
        print("coucou")