#!/usr/bin/env python3
import os
import pandas as pd
from typing import Tuple
from src.logger import CustomLogger


class CSVLoader:
    def __init__(self, product_path: str, sales_path: str, store_path: str):
        self.__product_path = f"{os.path.abspath('input_data')}/" + product_path
        self.__sales_path = f"{os.path.abspath('input_data')}/" + sales_path
        self.__store_path = f"{os.path.abspath('input_data')}/" + store_path

        self.__logger = CustomLogger(logger_name="DbReader").logger

    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        try:
            product_df = pd.read_csv(self.__product_path)
            sales_df = pd.read_csv(self.__sales_path)
            store_df = pd.read_csv(self.__store_path)
            return product_df, sales_df, store_df
        except FileNotFoundError as e:
            self.__logger.error(f"Error: {e}. Please check the file paths.")
        except pd.errors.EmptyDataError as e:
            self.__logger.error(f"Error: {e}. One of the files is empty.")
        except Exception as e:
            self.__logger.error(f"An unexpected error durring loading files occurred: {e}")
