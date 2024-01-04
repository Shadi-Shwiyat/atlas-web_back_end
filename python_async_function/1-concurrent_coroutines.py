#!/usr/bin/env python3
'''Script calls wait_random n amount of times
    and then returns a list of all the values
    spawned by wait_random'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''n and max_delay should be passed as an int,
    and this function will return a list of floats
    that were returned by the wait_random function'''
    float_list = []
    calls: int = 0
    while calls < n:
        delay_result = await wait_random(max_delay)
        float_list.append(delay_result)
        calls += 1
    return float_list
