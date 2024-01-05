#!/usr/bin/env python3
'''Script builds upon task 0 to build a list
    of 10 random numbers and return the list'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''coroutine that collects 10 random
    floats using async comprehensing over
    async_generator, then return the list of 10 floats'''
    results = []
    async for result in async_generator():
        results.append(result)
    return results
