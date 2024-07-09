#!/usr/bin/env python3
"""
    0-basic_async_syntax.py
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random"""
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
