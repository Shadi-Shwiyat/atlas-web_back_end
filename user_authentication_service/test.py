#!/usr/bin/env python3
import re

def example_function(**kwargs):
    # Accessing the value of the "name" keyword argument
    name_value = kwargs.get("name")
    print(f"Name: {name_value}")

# Calling the function with keyword arguments
example_function(name="John", age=25, city="ExampleCity")