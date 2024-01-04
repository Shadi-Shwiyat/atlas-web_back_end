#!/usr/bin/env python3
'''Script uses asynchronous coroutine
    named wait_random that takes in an
    int argument and waits for a random
    delay between 0 and the max_delay'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''max_delay is passed in as an int,
    and it should be the maximum time the
    async call should wait to return'''
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
