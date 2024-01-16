#!/usr/bin/env python3
'''Script implements a function
    that takes a string(password)
    and returns a hashed password
    as a byte string'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''function takes in a password
        and returns it as a hashed
        byte string'''
    byte_string = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_string, bcrypt.gensalt())
    return(hashed_password)
