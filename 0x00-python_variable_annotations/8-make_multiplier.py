#!/usr/bin/env python3
"""takes a float multiplier as argument and returns a function that multiplies
a float by multiplier"""
from typing import Callable


def make_mulitpler(multiplier: float) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
