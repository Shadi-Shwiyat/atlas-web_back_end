#!/usr/bin/env python3
'''
Session authentication class
inherits from base Auth class
'''
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
import os
import uuid
import base64


class SessionAuth(Auth):
    '''Class builds upon base Auth
        class to implement a session
        authentication'''

    user_id_by_session_id: dict = {}

    def __init__(self) -> None:
        '''Constructor method, use
            super to inherit from parent
            class'''
        super().__init__()

    def create_session(self,
                       user_id: str = None
                       ) -> str:
        '''Creates a session ID
            for a user_id'''
        if (not user_id or
           not isinstance(user_id, str)):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self,
                               session_id: str = None
                               ) -> str:
        '''Returns a user id
            based on session id'''
        if (not session_id or
           not isinstance(session_id, str)):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        '''returns a user instance
            based on a cookie value'''
        session_cookie = str(self.session_cookie(request))
        # print('session cookie is:', session_cookie)
        current_user = self.user_id_for_session_id(session_cookie)
        # print('current user is:', current_user)

        user_cls = User()
        user = user_cls.get(current_user)
        # print('user is:', user)

        return user
