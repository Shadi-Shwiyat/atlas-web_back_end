#!/usr/bin/env python3
'''Authentication class'''
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


def _hash_password(password: str) -> bytes:
    '''Returns a hashed version of passed in pwd'''
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                    bcrypt.gensalt())
    return hashed_password


def _generate_uuid() -> str:
    '''Returns string representing the
        new UUID'''
    return str(uuid.uuid4())


class Auth():
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str,
                      password: str) -> User:
        '''Returns user object after creating
        user, if they already exits then raises
        a ValueError'''
        try:
            already_exist = self._db.find_user_by(email=email)
            if already_exist:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        '''Checks credentials and returns true if valid,
            otherwise returns false'''
        try:
            user = self._db.find_user_by(email=email)
            # print(user)
            hashed_password = password.encode('utf-8')
            # print(f"hashed password is: {hashed_password},
            # database hashed password is: {user.hashed_password}")
            password_check = bcrypt.checkpw(hashed_password,
                                            user.hashed_password)
            return password_check
        except (NoResultFound, InvalidRequestError):
            # print('no user found')
            return False

    def create_session(self, email: str) -> str:
        '''Creates and returns a session ID
            based on passed in email'''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                new_session_id = _generate_uuid()
                user.session_id = new_session_id
                return new_session_id
        except (NoResultFound, InvalidRequestError):
            # print('no user found')
            return None
