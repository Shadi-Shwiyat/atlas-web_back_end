#!/usr/bin/env python3
'''Function takes a mixed list
    of ints and floats and
    returns their sum as a float'''
from typing import *


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Annotate mxd_lst as a union list of ints
    and floats to accept either, sum the list and
    return the value as a float'''
    list_sum = sum(mxd_lst)
    return list_sum
