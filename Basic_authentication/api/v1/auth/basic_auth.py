#!/usr/bin/env python3
'''Module holds basic
    authentication class'''
from flask import request
from typing import List
from typing import TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''An implementation
        of a basic authentication system'''
    def __init__(self) -> None:
        '''Constructor method,
            inherits from parent'''
        super().__init__()
