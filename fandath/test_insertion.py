# -*- coding: utf-8 -*-

import wisdomhord
from wisdomhord import Bisen, Sweor
import unittest
import os
import datetime

PATH_TO_WH = os.path.join(os.path.dirname(__file__), "insertion_test.hord")

class TestBisen(Bisen):

    __invoker__ = 'Wísdómhord Insertion Testing'
    __description__ = 'Insertion Test For Wísdómhord'

    col1 = Sweor('COL1', wisdomhord.String)
    col2 = Sweor('COL2', wisdomhord.Boolean)
    col3 = Sweor('COL3', wisdomhord.Integer)
    col4 = Sweor('COL4', wisdomhord.Float)
    col5 = Sweor('COL5', wisdomhord.DateTime)


class TestWisdomhordReading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hord = wisdomhord.cennan(PATH_TO_WH, bisen=TestBisen)

    @classmethod
    def tearDownClass(cls):
        os.remove(PATH_TO_WH)

    def test_insertion(self):
        row = {'COL1': 'Hello!',
               'COL2': True,
               'COL3': 10,
               'COL4': 20.3,
               'COL5': datetime.datetime.now()}

        self.hord.insert(row)

        rows = self.hord.get_rows()
        for k, v in row.items():
            self.assertEqual(v, rows[0][k])
