#!/usr/bin/env python3
import re

def extract_values_from_kwargs(**kwargs):
    # Define a regular expression pattern to match values
    value_pattern = re.compile(r'(?P<value>\w+)')

    extracted_values = {}
    for key, value in kwargs.items():
        # Use regular expression to extract values
        match = value_pattern.search(str(value))
        if match:
            extracted_values[key] = match.group('value')

    return extracted_values

# Example usage:
kwargs = {'param1': 'value123', 'param2': 'another456', 'param3': 'last789'}
result = extract_values_from_kwargs(**kwargs)
print(result)