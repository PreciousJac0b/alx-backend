#!/usr/bin/env python3

""" Simple Pagination. """

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Simple Pagination. """
    multiplier: int = page - 1
    return (multiplier * page_size, page * page_size)


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
        """ Gets Paginated pages from a CSV file. """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, stop_index = index_range(page, page_size)
        values: List = []

        with open(self.DATA_FILE) as file:
            reader = csv.reader(file)
            if start_index > 19419:
                return []
            for index, row in enumerate(reader, start=1):
                if start_index < index <= stop_index:
                    values.append(row)

            return values

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns a dict containing some particular methods. """
        page_begin, page_end = index_range(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        return {
            "page_size": page_size if page_size <= len(data) else len(data),
            "page": page_begin,
            "data": data,
            "next_page": page_begin + 1 if page_begin <= total_pages else None,
            "prev_page": page_begin - 1 if page_begin > 1 else None,
            "total_pages": total_pages
        }
