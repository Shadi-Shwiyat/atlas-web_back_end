#!/usr/bin/env python3
'''Unittest module for utils.py'''
import unittest
import requests
from unittest.mock import (
    patch,
    PropertyMock,
    MagicMock
)
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}},
         'my_license',
         True),
        ({"license": {"key": "other_license"}},
         'my_license',
         False),
    ])
    def test_has_license(self, license, license_key,
                         expected_result):
        '''Testing has_license static method'''
        client = GithubOrgClient('org')
        result = client.has_license(license, license_key)

        self.assertEqual(result, expected_result)


@parameterized_class([
    {'org_payload': TEST_PAYLOAD[0][0]},
    {'repos_payload': TEST_PAYLOAD[0][1]},
    {'expected_repos': TEST_PAYLOAD[0][2]},
    {'apache2_repos': TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Inherits from testcase,
        integration test class for
        public_repos method'''
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @classmethod
    def setUpClass(cls):
        '''Sets up the class
        with parameters for test'''
        # print('org_payload is:', TEST_PAYLOAD[0][0])
        # print('repos_payload is:', TEST_PAYLOAD[0][1])
        # print('expected_repos is:', TEST_PAYLOAD[0][2])
        # print('apache2_repos is:', TEST_PAYLOAD[0][3])
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Set side effects for different URLs
        cls.mock_get.side_effect = [
            MagicMock(json=lambda: cls.org_payload),
            MagicMock(json=lambda: cls.repos_payload),
            MagicMock(json=lambda: cls.apache2_repos)
        ]

    @classmethod
    def tearDownClass(cls):
        '''Tears down class to prep
        for next test'''
        cls.get_patcher.stop()

    # def test_example1(self):
    #     '''Testing payload output'''
    #     print('setup called to print payloads')


if __name__ == "__main__":
    unittest.main()
