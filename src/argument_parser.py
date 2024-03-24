#!/usr/bin/env python3
import argparse
from typing import Tuple
from datetime import datetime


class ArgumentParserWrapper:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="Analyze top sellers in given date range")
        self._initialize_arguments()

    def _initialize_arguments(self):
        self._parser.add_argument("--min-date", type=str, default="2020-01-01",
                                 help="Start of the date range in YYYY-MM-DD format")
        self._parser.add_argument("--max-date", type=str, default="2020-06-30",
                                 help="End of the date range in YYYY-MM-DD format")
        self._parser.add_argument("--top", type=int, default=3, help="Number of top items to display")

    def get_dates(self, args) -> Tuple[datetime, datetime]:
        min_date = datetime.strptime(args.min_date, "%Y-%m-%d")
        max_date = datetime.strptime(args.max_date, "%Y-%m-%d")
        return min_date, max_date

    def parse(self, args=None):
        return self._parser.parse_args(args)
