#!/usr/bin/env python3
from src.csv_loader import CSVLoader
from src.df_analyzer import DataFrameAnalyzer, AnalysisParameters
from src.argument_parser import ArgumentParserWrapper

if __name__ == "__main__":
    arg_parser = ArgumentParserWrapper()
    args = arg_parser.parse()

    min_date, max_date = arg_parser.get_dates(args)
    params = AnalysisParameters(min_date=min_date, max_date=max_date, top=args.top)

    loader = CSVLoader('product.csv', 'sales.csv', 'store.csv')
    product_df, sales_df, store_df = loader.load_data()

    analyzer = DataFrameAnalyzer(product_df, sales_df, store_df, params)
    analyzer.display()