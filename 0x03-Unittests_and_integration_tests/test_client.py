#!/usr/bin/env python3
"""Module to test the Github class"""
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
import unittest
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        expected = 'https://api.github.com/orgs/test-org/repos'
        mock_org.return_value = {'repos_url': expected}
        client = GithubOrgClient('test-org')
        self.assertEqual(client._public_repos_url, expected)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method"""
        expected_repos_url = 'https://api.github.com/orgs/test-org/repos'
        mock_public_repos_url.return_value = expected_repos_url
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = repos_payload
        client = GithubOrgClient('test-org')
        repos = client.public_repos()
        expected_repos = ["repo1", "repo2", "repo3"]
        self.assertEqual(repos, expected_repos)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(expected_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        client = GithubOrgClient('test')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


class MockResponse:
    """Mock class to simulate responses from requests.get"""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """An integration test for the GithubOrgClient.public_repos"""
    @classmethod
    def setUpClass(cls) -> None:
        """Setups the test class"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mock_requests_get

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleans the class after testing"""
        cls.get_patcher.stop()

    @staticmethod
    def mock_requests_get(url, *args, **kwargs):
        """Mock requests.get to return different payloads based on the URL"""
        if url == "https://api.github.com/orgs/test-org":
            return MockResponse(org_payload)
        elif url == "https://api.github.com/orgs/test-org/repos":
            return MockResponse(repos_payload)
        else:
            raise ValueError(f"Unexpected URL: {url}")

    def test_public_repos(self):
        """Test public_repos method integration"""
        client = GithubOrgClient('test-org')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with specific license filter"""
        client = GithubOrgClient('test-org')
        repos = client.public_repos(license='apache2.0')
        self.assertEqual(repos, self.apache2_repos)
