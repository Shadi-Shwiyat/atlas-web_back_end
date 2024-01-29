#!/usr/bin/env python3
'''Unittest module for utils.py'''
import unittest
from unittest.mock import patch, MagicMock, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import requests
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    '''Inherits from testcase,
        unittest class for acces
        nested map function'''
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @parameterized.expand([
        ({'a': 1}, ('a',), (1)),
        ({'a': {'b': 2}}, ('a',), ({'b': 2})),
        ({'a': {'b': 2}}, ('a', 'b'), (2))
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected_result: Any
                               ) -> Any:
        '''Method asserts that output of
            access_nested_map is as expected'''
        result = access_nested_map(nested_map, path)
        # print(result)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ('a',), (KeyError)),
        ({'a': 1}, ('a', 'b'), (KeyError))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected_result: Any
                                         ) -> None:
        '''Method catches any errors
            raised by access_nested_map'''
        with self.assertRaises(expected_result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Inherits from testcase,
        unittest class for get json
        function'''
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self,
                      url: str, payload: Dict[str, bool],
                      mock_requests: MagicMock
                      ) -> None:
        '''Method asserts that output of
            get_json is as expected and mocks
            the request output in get_json'''
        mock_requests.return_value.json.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    '''Inherits from testcase,
        unittest class for memoize
        function'''
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_memoize(self
                     ) -> None:
        '''Method asserts that output of
            memoize is as expected'''

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property,
                             mock_method.return_value)
            self.assertEqual(instance.a_property,
                             mock_method.return_value)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
