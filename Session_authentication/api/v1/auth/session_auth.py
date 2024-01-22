#!/usr/bin/env python3
'''
Session authentication class
inherits from base Auth class
'''
from api.v1.auth.auth import Auth
import uuid


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
