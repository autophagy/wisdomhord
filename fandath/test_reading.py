# -*- coding: utf-8 -*-

import wisdomhord
from wisdomhord import Bisen, Sweor
import unittest
import os
import datetime
import datarum

PATH_TO_WH = os.path.join(os.path.dirname(__file__), "test.hord")


class TestBisen(Bisen):

    __invoker__ = "Wísdómhord Testing"
    __description__ = "Test data for Wísdómhord"

    col1 = Sweor("COL1", wisdomhord.String)
    col2 = Sweor("COL2", wisdomhord.Integer)
    col3 = Sweor("COL3", wisdomhord.Boolean)
    col4 = Sweor("COL4", wisdomhord.String)
    col5 = Sweor("COL5", wisdomhord.DateTime)
    col6 = Sweor("COL6", wisdomhord.Wending)


class TestWisdomhordReading(unittest.TestCase):

    expected_meta = {
        "INVOKER": "Wísdómhord Testing",
        "DESCRIPTION": "Test data for Wísdómhord",
        "INCEPT": "9 Regn 226 // 03.40",
        "UPDATED": "9 Regn 226 // 04.00",
        "COUNT": "7",
    }

    expected_keys = ["COL1", "COL2", "COL3", "COL4", "COL5", "COL6"]

    expected_column_lengths = {
        "COL1": 13,
        "COL2": 5,
        "COL3": 5,
        "COL4": 11,
        "COL5": 22,
        "COL6": 26,
    }

    @classmethod
    def setUpClass(cls):
        cls.hord = wisdomhord.hladan(PATH_TO_WH, bisen=TestBisen)

    def test_get_metadata(self):
        for k, v in self.expected_meta.items():
            self.assertEqual(self.hord.meta[k], v)

    def test_get_keys(self):
        self.assertEqual(self.expected_keys, self.hord.keys)

    def test_get_column_lengths(self):
        for k, v in self.expected_column_lengths.items():
            self.assertEqual(self.hord._column_lengths[k], v)

    def test_key_row(self):
        self.assertEqual(self.hord._key_row, 6)

    def test_get_first_row(self):
        expected_row = {
            "col1": "Hello world",
            "col2": 12345,
            "col3": True,
            "col4": "If",
            "col5": datetime.datetime(2018, 2, 16, 12, 15, 15),
            "col6": datarum.wending(226, 5, 28, 12, 11, 15),
        }

        row = self.hord.get_rows(limit=1)
        self.assertEqual(len(row), 1)

        for k, v in expected_row.items():
            self.assertEqual(v, getattr(row[0], k))

    def test_multiple_rows(self):
        rows = self.hord.get_rows(limit=4)
        self.assertEqual(len(rows), 4)

    def test_get_all_rows(self):
        rows = self.hord.get_rows()
        self.assertEqual(len(rows), self.hord.row_count())

    def test_get_specific_cols(self):
        expected_row = {"col2": 12345, "col3": True}

        row = self.hord.get_rows(cols=["COL2", "COL3"], limit=1)

        for k, v in expected_row.items():
            self.assertEqual(v, getattr(row[0], k))

    def test_filter(self):
        filter_func = lambda row: row.col3 == True
        rows = self.hord.get_rows(filter_func=filter_func)

        self.assertEqual(len(rows), 4)

        for row in rows:
            self.assertEqual(row.col3, True)

    def test_sort(self):
        rows = self.hord.get_rows(cols=["COL4"])
        col_to_sort = list(map(lambda x: x.col4, rows))

        sorted_col = sorted(col_to_sort)
        reverse_sorted_col = sorted(col_to_sort, reverse=True)

        sorted_rows = self.hord.get_rows(sort_by=TestBisen.col4)
        reverse_sorted_rows = self.hord.get_rows(
            sort_by=TestBisen.col4, reverse_sort=True
        )

        for i, row in enumerate(sorted_rows):
            self.assertEqual(row.col4, sorted_col[i])

        for i, row in enumerate(reverse_sorted_rows):
            self.assertEqual(row.col4, reverse_sorted_col[i])
