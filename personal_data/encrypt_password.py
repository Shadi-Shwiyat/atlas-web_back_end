#!/usr/bin/env python3
'''Script functions that hash
    a password, and then validate
    a hashed password'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''function takes in a password
        and returns it as a hashed
        byte string'''
    byte_string = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_string, bcrypt.gensalt())
    return(hashed_password)


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''function validates the provided
        password against the hashed_password'''
    byte_string = password.encode('utf-8')
    if bcrypt.checkpw(byte_string, hashed_password):
        return True
    else:
        return False
