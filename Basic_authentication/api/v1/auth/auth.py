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
        return False

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
