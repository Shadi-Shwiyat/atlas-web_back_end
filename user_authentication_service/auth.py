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

    def get_user_from_session_id(self,
                                 session_id: str
                                 ) -> User or None:
        '''Takes in the session id and
            finds the user corresponding to that
            id'''
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except (NoResultFound, InvalidRequestError):
            return None

    def destroy_session(self,
                        user_id: int
                        ) -> None:
        '''Destroys the users session
            based on their id'''
        try:
            user = self._db.find_user_by(id=user_id)
            if user:
                user.session_id = None
        except (NoResultFound, InvalidRequestError):
            return None

    def get_reset_password_token(self, email: str) -> str:
        '''Generates uuid for user and sets
            the user.reset_token field to the
            new uuid'''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                reset_token = uuid.uuid4()
                user.reset_token = reset_token
                return reset_token
        except (NoResultFound, InvalidRequestError):
            raise ValueError()
