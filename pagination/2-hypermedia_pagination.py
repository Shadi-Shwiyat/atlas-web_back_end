#!/usr/bin/env python3
'''Module builds a class that
    uses a data.csv file and
    paginates the data from that
    file, task 2 implements
    hypermedia pagination'''
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


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
        '''Returns a list of items in the
            appropriate page of the dataset(.csv file)'''
        assert (type(page) == int and type(page_size) == int), "Error"
        assert (page > 0 and page_size > 0), "Error"

        result_list = []
        page_indexes = index_range(page, page_size)
        dataset = self.dataset()

        dataset_length = len(dataset)
        # print(dataset_length)

        for index in range(page_indexes[0], page_indexes[1]):
            if index > dataset_length:
                return result_list
            else:
                result_list.append(dataset[index])

        return result_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Returns a dictionary containing prev and next
            pages, total amount of pages, and the dataset
            of the current page.'''
        current_page_data = self.get_page(page, page_size)

        dataset = self.dataset()
        total_pages = math.ceil((len(dataset) / page_size))

        if ((page - 1) <= 0):
            prev_page = None
        else:
            prev_page = page - 1

        if ((page + 1) > total_pages):
            next_page = None
        else:
            next_page = page + 1

        return {
            'page_size': page_size,
            'page': page,
            'data': current_page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
