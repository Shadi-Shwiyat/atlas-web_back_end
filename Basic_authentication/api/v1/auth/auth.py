#!/usr/bin/env python3
'''Module holds basic
    authentication class'''
from flask import request
from typing import List
from typing import TypeVar


class Auth():
    '''An implementation
        of a basic authentication system'''

    def __init__(self) -> None:
        '''Constructor method of auth class'''

    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        '''Public method that
            returns a boolean if path
            requires authorization'''
        if path is None:
            # print('path is None')
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            # print("excluded paths is None or empty")
            return True
        elif path in excluded_paths:
            # print('path is in excluded paths')
            return False
        elif (path + "/") in excluded_paths:
            # print('path + / is in excluded paths')
            return False
        elif path not in excluded_paths:
            # print('path not in excluded paths')
            return True

    def authorization_header(self,
                             request=None) -> str:
        '''Public method that
            will return the auth
            header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Public method will return
            the current user'''
        return None
