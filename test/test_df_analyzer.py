#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from datetime import datetime
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from src.transform.df_analyzer import DataFrameAnalyzer, AnalysisParameters


class TestDataFrameAnalyzer(unittest.TestCase):

    def setUp(self):
        self.product_df = DataFrame({'id': [1, 2], 'name': ['Product A', 'Product B']})
        self.sales_df = DataFrame({'date': ['2023-01-01', '2023-02-01'], 'product': [1, 2], 'quantity': [10, 20]})
        self.store_df = DataFrame({'id': [1, 2], 'name': ['Store A', 'Store B']})
        self.params = AnalysisParameters(datetime(2023, 1, 1), datetime(2023, 3, 1), 2)

    def test_init(self):
        analyzer = DataFrameAnalyzer(self.product_df, self.sales_df, self.store_df, self.params)
        self.assertIsNotNone(analyzer)

    @patch.object(DataFrameAnalyzer, '_DataFrameAnalyzer__filter_and_merge',
                  return_value=DataFrame({'product': [1, 2], 'quantity': [10, 20]}))
    def test_filter_and_merge(self):
        analyzer = DataFrameAnalyzer(self.product_df, self.sales_df, self.store_df, self.params)
        result_df = analyzer._DataFrameAnalyzer__filter_and_merge()
        expected_df = DataFrame({'product': [1, 2], 'quantity': [10, 20]})
        assert_frame_equal(result_df, expected_df)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
