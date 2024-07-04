#!/usr/bin/env python3
"""Returns the sum of a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: int = 0
    for x in input_list:
        sum += x
    return float(sum)
