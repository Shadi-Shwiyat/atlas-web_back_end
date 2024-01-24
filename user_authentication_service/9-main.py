#!/usr/bin/env python3
"""
Main file
"""
from auth import _generate_uuid

new_id = _generate_uuid()
print(new_id)
print(type(new_id))
