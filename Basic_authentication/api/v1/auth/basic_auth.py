#!/usr/bin/env python3
'''Module holds basic
    authentication class'''
from flask import request
from typing import List
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        '''Method returns decoded value
            of a Base64 string'''
        if (not base64_authorization_header or
           not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError) as e:
            # print(f"Error decoding base64: {e}")
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        '''Method returns the user
            email and password from
            Base64 decoded value'''
        if (not decoded_base64_authorization_header or
           not isinstance(decoded_base64_authorization_header, str) or
           ':' not in decoded_base64_authorization_header):
            return (None, None)
        else:
            semi_col_index = decoded_base64_authorization_header.find(':')
            email = decoded_base64_authorization_header[:semi_col_index]
            password = decoded_base64_authorization_header[(semi_col_index
                                                            + 1):]
            return (email, password)
