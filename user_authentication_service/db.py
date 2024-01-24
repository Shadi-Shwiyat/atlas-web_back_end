#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """
    total_users = 0

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self,
                 email: str,
                 hashed_password: str
                 ) -> User:
        '''Adds user to db and returns
            user object'''
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self.total_users += 1
        user.id = self.total_users

        session = self._session
        session.add(user)
        session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        '''Returns first row found
            in users table filtered by
            the methods input kwargs'''
        user_class = User
        session = self._session
        try:
            user = session.query(user_class).filter_by(**kwargs).one()
            return user
        except (NoResultFound, InvalidRequestError) as error:
            raise error

    def update_user(self, user_id: int,
                    **kwargs) -> None:
        '''Updates user based on given ID
            and the given kwargs to update'''
        user = self.find_user_by(id=user_id)
        session = self._session
        # print(user.hashed_password)
        email = kwargs.get('email')
        hsh_pwd = kwargs.get('hashed_password')
        if (not email and not hsh_pwd):
            raise ValueError
        elif not email:
            try:
                user.hashed_password = hsh_pwd
                session.commit()
            except ValueError as e:
                raise e
        elif not hsh_pwd:
            try:
                user.email = email
                session.commit()
            except ValueError as e:
                raise e
