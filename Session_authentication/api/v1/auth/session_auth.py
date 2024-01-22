#!/usr/bin/env python3
'''
Session authentication class
inherits from base Auth class
'''
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    '''Class builds upon base Auth
        class to implement a session
        authentication'''
    def __init__(self) -> None:
        '''Constructor method, use
            super to inherit from parent
            class'''
        super().__init__()
