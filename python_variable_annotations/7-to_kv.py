#!/usr/bin/env python3
'''Function takes a string AND an int OR a float
    as arguments and returns a tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''k is a string, v can be int or float,
    return a tuple where the first element is k
    and the second element is v squared. v should be a float
    in the tuple'''
    new_tuple = tuple()
    new_tuple = [k, (v*v)]
    return new_tuple
