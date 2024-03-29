#!/usr/bin/env python3
"""performing python function in pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """ calculating the starting and ending indexes
    params:
    page: page number
    page_size: number of items per page
    return: tuple containing start and end indexes
    """

    if page <= 0 or page_size <= 0:
        raise ValueError("page and page_size must be positive")

    s_index = (page - 1) * page_size
    e_index = s_index + page_size

    return (s_index, e_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Getting specific page of the dataset
        params:
        page: page number
        page_size: number of items per page
        return: list representing page of the dataset
        """

        assert (
            isinstance(page, int) and page > 0
        ), "page must be a positive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be a positive integer"

        s_index, e_index = index_range(page, page_size)
        dataset = self.dataset()

        if s_index >= len(dataset):
            return []

        return dataset[s_index:min(e_index + 1, len(dataset))]
