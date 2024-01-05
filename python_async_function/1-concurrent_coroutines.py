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

    async def wait_and_append():
        result = await wait_random(max_delay)
        float_list.append(result)

    # Create tasks and add them to the event loop
    tasks = [asyncio.create_task(wait_and_append()) for _ in range(n)]

    # Use asyncio.gather to wait for all tasks to complete
    await asyncio.gather(*tasks)

    return float_list
