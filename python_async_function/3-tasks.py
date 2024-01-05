#!/usr/bin/env python3
'''Script that takes a int(max_delay)
    and returns a call to the function wait_random
    using an asyncio.Task'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Regular function returns a call to the wait_random
    using asyincio.Task'''
    function_call = asyncio.create_task(wait_random(max_delay))
    return function_call
