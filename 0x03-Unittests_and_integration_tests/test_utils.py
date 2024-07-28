#!/usr/bin/env python3
"""Module to test the access_nested_map function"""
from utils import access_nested_map
from typing import Mapping, Sequence
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Module  for the test function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: any) -> any:
        self.assertEqual(access_nested_map(nested_map, path), expected)
