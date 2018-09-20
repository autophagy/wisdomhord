# -*- coding: utf-8 -*-

import wisdomhord
from wisdomhord import Bisen, Sweor
import unittest
import os
import datarum

PATH_TO_WH = os.path.join(os.path.dirname(__file__), "creation_test.hord")


class TestBisen(Bisen):

    __invoker__ = "Wísdómhord Creation Testing"
    __description__ = "Creation Test For Wísdómhord"

    col1 = Sweor("COL1", wisdomhord.String)
    col2 = Sweor("COL2", wisdomhord.Integer)
    col3 = Sweor("COL3", wisdomhord.Boolean)
    col4 = Sweor("COL4", wisdomhord.String)


class TestWisdomhordReading(unittest.TestCase):

    expected_meta = {
        "INVOKER": "Wísdómhord Creation Testing",
        "DESCRIPTION": "Creation Test For Wísdómhord",
        "COUNT": "0",
    }

    expected_keys = ["COL1", "COL2", "COL3", "COL4"]

    @classmethod
    def setUpClass(cls):
        # This also tests whether the hord can be loaded after creation
        wisdomhord.cennan(PATH_TO_WH, bisen=TestBisen)
        cls.hord = wisdomhord.hladan(PATH_TO_WH, bisen=TestBisen)

    @classmethod
    def tearDownClass(cls):
        os.remove(PATH_TO_WH)

    def test_get_metadata(self):
        for k, v in self.expected_meta.items():
            self.assertEqual(self.hord.meta[k], v)

    def test_get_keys(self):
        self.assertEqual(self.expected_keys, self.hord.keys)

    def test_correct_wending(self):
        today = datarum.wending.now().strftime(
            "{daeg} {month} {gere} // {tid_zero}.{minute_zero}"
        )
        self.assertEqual(self.hord.meta["INCEPT"], today)
        self.assertEqual(self.hord.meta["UPDATED"], today)
