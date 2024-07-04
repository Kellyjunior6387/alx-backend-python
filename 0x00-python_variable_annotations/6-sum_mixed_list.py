#!/usr/bin/env python3
""" takes a list mxd_lst of integers and floats and returns
their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Python annotations
    """
    sum: int = 0
    for x in mxd_list:
        sum += x
    return float(sum)
