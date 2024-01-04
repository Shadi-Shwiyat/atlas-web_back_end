#!/usr/bin/env python3
'''Function returns the length of a list'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''lst is a iterable list of squences(e.g. a list, tuple, etc),
    the function returns a list of tuples. the first tuple element is the
    original sequence passed in, while the second tuple element is a int lenght
    of the first element sequence'''
    return [(i, len(i)) for i in lst]
