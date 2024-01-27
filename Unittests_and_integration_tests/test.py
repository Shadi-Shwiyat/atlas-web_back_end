#!/usr/bin/env python3
from utils import access_nested_map, get_json, memoize
import requests

# nested_map = {"a": {"b": {"c": {"d": 6}}}}
# print(access_nested_map(nested_map, ["a", "b", "c", 'd']))

url = "http://holberton.io"

def get_json(url: str):
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()

print(get_json(url))