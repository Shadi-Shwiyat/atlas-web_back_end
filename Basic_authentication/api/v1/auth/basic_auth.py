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

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Method returns the Base64 part
            or the Authorization header'''
        if (not authorization_header or
           not isinstance(authorization_header, str) or
           not authorization_header.startswith('Basic ')):
            return None
        else:
            return authorization_header[len('Basic '):]
