#!/usr/bin/env python3
'''Function determines total execution
    time when calling wait_n function and then
    returns total time by the number of calls
    to get the average time'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''n and max delay should be ints, function
    will determine total runtime using time module
    and return the average time using total_time / n'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time / n)
