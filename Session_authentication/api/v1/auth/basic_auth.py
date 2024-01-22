#!/usr/bin/env python3
'''Module holds basic
    authentication class'''
from flask import request
from typing import List
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import json
import base64
import binascii


def read_json_file(file_path):
    '''Function reads a json file
        to later use the data in
        BasicAuth class'''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


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

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        '''Returns the User instance
            based on user's email and
            password'''
        user_data = read_json_file('.db_User.json')
        if (not user_email or
           not user_pwd or
           not isinstance(user_email, str) or
           not isinstance(user_pwd, str) or
           not user_data or
           len(user_data) < 1):
            # print('user/email/password doesnt exist or not a string')
            return None
        user_cls = User(email=user_email)
        user_cls.password = user_pwd

        matching_users = user_cls.search(attributes={'email': user_email})
        if matching_users:
            for user in matching_users:
                if user.is_valid_password(user_pwd):
                    return user
        else:
            # print("User not found.")
            return None

    def current_user(self,
                     request=None) -> TypeVar('User'):
        '''Method overloads Auth and retrieves the
            User instance for a request'''
        auth = BasicAuth()
        header = auth.authorization_header(request)
        base64_header = auth.extract_base64_authorization_header(header)
        decode_header = auth.decode_base64_authorization_header(base64_header)
        user_credentials = auth.extract_user_credentials(decode_header)
        user = auth.user_object_from_credentials(user_credentials[0],
                                                 user_credentials[1])

        return user
