#!/usr/bin/env python3
"""Function to mention an await"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure a coroutine
    """
    start = time.perf_counter
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter
    total = end - start
    return total / n
