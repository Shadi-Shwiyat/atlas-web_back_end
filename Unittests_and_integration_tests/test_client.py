#!/usr/bin/env python3
'''Unittest module for utils.py'''
import unittest
from unittest.mock import (
    patch,
    MagicMock,
    Mock,
    PropertyMock
)
from client import GithubOrgClient
from parameterized import parameterized
import requests
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestGithubOrgClient(unittest.TestCase):
    '''Inherits from testcase,
        unittest class for GithubOrgClient
        method'''
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={'some': 'data'})
    def test_org(self, org_name, mock_get_json):
        '''Testing the org method'''
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org

        self.assertEqual(result, {'some': 'data'})

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    @patch('client.GithubOrgClient.org',
           PropertyMock(return_value={
               'repos_url': 'https://api.github.com/orgs/org/repos'
               }))
    def test_public_repos_url(self):
        '''Testing the public repo property'''
        client = GithubOrgClient('org')
        # print('mocked org returns:', client.org['repos_url'])

        result = client._public_repos_url
        # print('result is:', result)
        self.assertEqual(result, 'https://api.github.com/orgs/org/repos')

    @patch('client.get_json',
           return_value=[
               {'name': 'repo1'},
               {'name': 'repo2'},
               {'name': 'repo3'}])
    @patch('client.GithubOrgClient.org',
           new_callable=PropertyMock,
           return_value={
               'repos_url': 'https://api.github.com/orgs/org/repos'
           })
    def test_public_repos(self, mock_org, mock_get_json):
        '''Testing the public repos method'''
        client = GithubOrgClient('org')

        result = client.public_repos()

        self.assertEqual(result, [
            'repo1',
            'repo2',
            'repo3'
        ])
        mock_get_json.assert_called_once()
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
