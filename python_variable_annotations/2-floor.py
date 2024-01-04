#!/usr/bin/env python3
'''Function takes a float 'n' as arguement
    and returns the floor of the float
'''


def floor(n: float) -> int:
    '''Use annotation to hint n is a float
    and function is returning an integer as the floor.
    Check for floor using a loop as long as i + 1 is less that n
    than it is the floor(largest int that is less than or equal to
    the float)'''
    i = 0
    while i + 1 < n:
        i += 1
    
    return i
