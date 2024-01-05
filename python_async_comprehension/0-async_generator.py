#!/usr/bin/env python3
'''Script create an async generator'''
import asyncio
import random


async def async_generator() -> float:
    '''function loops 10 times, each time
    has an asynchronous wait for 1 second, and yeild
    a random float between 0 and 10'''
    async for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
