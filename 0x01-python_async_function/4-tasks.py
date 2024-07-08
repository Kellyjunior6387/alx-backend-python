#!/usr/bin/env python3
"""Function that uses asychronus"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that imports wait_random and run n times
    """
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    return delays
