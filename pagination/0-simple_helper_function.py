#!/usr/bin/env python3
'''Script builds a helper function
    that is used to determine the
    amount of indexes based on which
    page and page_size user is on'''


def index_range(page: int, page_size: int) -> tuple:
    '''page is the page number, and page_size is
        how many indexes should be on each page'''
    start_index: int = ((page - 1) * page_size)
    end_index: int = page * page_size
    range: tuple = (start_index, end_index)
    return range
