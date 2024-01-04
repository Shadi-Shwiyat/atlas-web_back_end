#!/usr/bin/env python3
'''Function takes a list of floats
    as arguments and returns their
    sum as a float. import typing module
    to use list typing of floats
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''input_list is a list of floats,
    calculate their sum and return a float(total)'''
    total = sum(input_list)
    return total
