#!/usr/bin/env python3
from utils import access_nested_map, get_json, memoize

nested_map = {"a": {"b": {"c": {"d": 6}}}}
print(access_nested_map(nested_map, ["a", "b", "c", 'd']))