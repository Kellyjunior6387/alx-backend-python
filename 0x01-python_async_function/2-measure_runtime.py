#!/usr/bin/env python3
'''Function to measure time.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the runtime of a asychronoys function.
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
