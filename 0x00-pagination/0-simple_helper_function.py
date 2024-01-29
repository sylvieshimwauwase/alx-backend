#!/usr/bin/env python3
"""performing python function in pagination"""


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
