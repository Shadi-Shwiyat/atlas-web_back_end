#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Returns a dictionary that is
            resilient to deletion during
            new page request'''
        dataset = self.indexed_dataset()
        dataset_length = len(dataset)
        assert (index < (dataset_length - 1)), "error"
        # print(dataset[6])

        current_page_data = []
        if index in dataset:
            for item in range(index, page_size + index):
                if item in dataset:
                    current_page_data.append(dataset[item])
                else:
                    print("item not in dataset")
                    index += 1
            next_index = index + page_size
        else:
            index += 1
            for item in range(index, page_size + index):
                if item in dataset:
                    current_page_data.append(dataset[item])
                else:
                    print("item not in dataset")
                    index += 1
            next_index = index + page_size
            index -= 1

        return {
            'index': index,
            'data': current_page_data,
            'page_size': page_size,
            'next_index': next_index
        }
