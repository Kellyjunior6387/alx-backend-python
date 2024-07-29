#!/usr/bin/env python3
"""Module to test the Github class"""
from client import GithubOrgClient
from unittest.mock import patch
import unittest
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TetsGithuborgclient"""
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Function to tests the org method"""
        expected = {'repo': org_name}
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
