#!/usr/bin/env python3
'''Unittest module for utils.py'''
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    '''Inherits from testcase,
        unittest class for utils.py'''
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
                                         ) -> Any:
        '''Method catches any errors
            raised by access_nested_map'''
        result = access_nested_map(nested_map, path)
        self.assertRaises(result, expected_result)


if __name__ == "__main__":
    unittest.main()
