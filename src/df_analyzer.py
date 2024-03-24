#!/usr/bin/env python3
import pandas as pd
from typing import Tuple
from pandas import DataFrame
from datetime import datetime
from dataclasses import dataclass
from src.logger import CustomLogger


@dataclass
class AnalysisParameters:
    min_date: datetime
    max_date: datetime
    top: int


class DataFrameAnalyzer:
    def __init__(self, product_df, sales_df, store_df, params: AnalysisParameters):
        self.__product_df = product_df
        self.__sales_df = sales_df
        self.__store_df = store_df
        self.__params = params

        self.__logger = CustomLogger(logger_name="DbReader").logger

    def __filter_and_merge(self) -> DataFrame:
        try:
            self.__sales_df["date"] = pd.to_datetime(self.__sales_df["date"])
            filtered_sales = self.__sales_df[
                (self.__sales_df["date"] >= self.__params.min_date) & (
                            self.__sales_df["date"] <= self.__params.max_date)]
            merged_sales = filtered_sales.merge(self.__product_df, left_on="product", right_on="id").merge(
                self.__store_df,
                left_on="store",
                right_on="id")
        except Exception as e:
            self.__logger.error(f"Error during filtering or merging dataframes. {e}")

        return merged_sales

    def __analyze(self, merged_sales) -> Tuple[DataFrame, DataFrame, DataFrame, DataFrame]:
        try:
            top_products = merged_sales.groupby("name")["quantity"].sum().nlargest(self.__params.top)
            top_stores = merged_sales.groupby("name")["quantity"].sum().nlargest(self.__params.top)
            top_brands = merged_sales.groupby("brand")["quantity"].sum().nlargest(self.__params.top)
            top_cities = merged_sales.groupby("city")["quantity"].sum().nlargest(self.__params.top)
        except Exception as e:
            self.__logger.error(f"Error during analysis of merged data. {e}")

        return top_products, top_stores, top_brands, top_cities

    def __get_top_n_or_equal(self, df: DataFrame, group_by_column: str, sum_column: str, top_n: int) -> DataFrame:
        grouped = df.groupby(group_by_column)[sum_column].sum().reset_index()
        top_values = grouped[sum_column].nlargest(top_n).min()
        return grouped[grouped[sum_column] >= top_values]

    def _create_final_dfs(self) -> Tuple[DataFrame, DataFrame, DataFrame, DataFrame]:
        merged_sales = self.__filter_and_merge()

        top_products_df = self.__get_top_n_or_equal(merged_sales, "name_x", "quantity", self.__params.top).rename(columns={"name_x": "name"})
        top_stores_df = self.__get_top_n_or_equal(merged_sales, "name_y", "quantity", self.__params.top).rename(columns={"name_y": "name"})
        top_brands_df = self.__get_top_n_or_equal(merged_sales, "brand", "quantity", self.__params.top)
        top_cities_df = self.__get_top_n_or_equal(merged_sales, "city", "quantity", self.__params.top)

        return top_products_df, top_stores_df, top_brands_df, top_cities_df

    def display(self) -> None:
        top_products_df, top_stores_df, top_brands_df, top_cities_df = self._create_final_dfs()
        top_products_df = top_products_df.sort_values(by='quantity', ascending=False)
        top_stores_df = top_stores_df.sort_values(by='quantity', ascending=False)
        top_brands_df = top_brands_df.sort_values(by='quantity', ascending=False)
        top_cities_df = top_cities_df.sort_values(by='quantity', ascending=False)

        print("-- top seller product --")
        print(top_products_df.to_string(index=False))

        print("-- top seller store --")
        print(top_stores_df.to_string(index=False))

        print("-- top seller brand --")
        print(top_brands_df.to_string(index=False))

        print("-- top seller city --")
        print(top_cities_df.to_string(index=False))
