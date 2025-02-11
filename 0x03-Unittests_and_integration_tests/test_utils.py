#!/usr/bin/env python3
"""Module to test the access_nested_map function"""
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence
import unittest
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> any:
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """class to test the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: str, mock_get):
        """Function to test result of json"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """test class"""
    def a_method(self):
        """a method to return 42"""
        return 42

    @memoize
    def a_property(self):
        """A method to call a_method"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """class to test the memoise function"""
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """Function to test the memoisation wrapper"""
        test_instance = TestClass()
        first_call = test_instance.a_property
        second_call = test_instance.a_property
        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)
        mock_a_method.assert_called_once()
