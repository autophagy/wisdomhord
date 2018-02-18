# -*- coding: utf-8 -*-

import wisdomhord
from wisdomhord import Bisen, Sweor
import unittest
import os
import datetime
import datarum

PATH_TO_WH = os.path.join(os.path.dirname(__file__), "insertion_test.hord")

class TestBisen(Bisen):

    __invoker__ = 'Wísdómhord Insertion Testing'
    __description__ = 'Insertion Test For Wísdómhord'

    col1 = Sweor('STRING',   wisdomhord.String)
    col2 = Sweor('BOOLEAN',  wisdomhord.Boolean)
    col3 = Sweor('INTEGER',  wisdomhord.Integer)
    col4 = Sweor('FLOAT',    wisdomhord.Float)
    col5 = Sweor('DATETIME', wisdomhord.DateTime)
    col6 = Sweor('WENDING',  wisdomhord.Wending)


class TestWisdomhordReading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hord = wisdomhord.cennan(PATH_TO_WH, bisen=TestBisen)

    @classmethod
    def tearDownClass(cls):
        os.remove(PATH_TO_WH)

    def test_insertion(self):
        row = {'STRING':   'Hello!',
               'BOOLEAN':  True,
               'INTEGER':  10,
               'FLOAT':    20.3,
               'DATETIME': datetime.datetime(2018, 2, 16, 12, 11, 15),
               'WENDING':  datarum.wending(226, 5, 28, 12, 11, 15)}

        self.hord.insert(row)

        rows = self.hord.get_rows()
        for k, v in row.items():
            self.assertEqual(v, rows[0][k])
