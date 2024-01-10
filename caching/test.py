#!/usr/bin/env python3
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Get a list of insertion order keys
insertion_order_keys = list(my_dict.keys())

# Check if 'c' was the last item inserted
if insertion_order_keys.index('c') == len(my_dict) - 1:
    print("'c' was the last item inserted.")
else:
    print("'c' was not the last item inserted.")