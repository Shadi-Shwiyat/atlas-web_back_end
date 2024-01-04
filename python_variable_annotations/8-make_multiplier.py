#!/usr/bin/env python3
'''Function takes a float(multiplier) as argument and
    returns a function that multiplies a float
    by the (multiplier), use callable class from
    typing module for annotation'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''take the multiplier and return a function that
    multiplies it by a new float passed in'''
    def multiplierFun(factor: float) -> float:
        '''use the multiplier and raise it by the factor,
        then return the product'''
        return multiplier * factor

    return multiplierFun
