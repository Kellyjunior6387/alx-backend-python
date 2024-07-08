#!/usr/bin/env python3
"""Function that uses ayschronous python"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay
    """
    delay = random.uniform(0, max_delay)
    asyncio.sleep(delay)
    return delay
