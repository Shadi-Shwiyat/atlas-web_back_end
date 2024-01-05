#!/usr/bin/bash python3
'''Script runs async_comprehension function
    four times in parallel'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Function will run async_comprehension
    four times in parallel, measure the total
    runtime, and return the value as a float'''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
