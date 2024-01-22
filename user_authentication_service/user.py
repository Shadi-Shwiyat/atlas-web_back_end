#!/usr/bin/env python3
'''Creating sqlalchemy user table'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    '''user sqlalchemy model'''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(length=250), nullable=False)
    hashed_password = Column(String(length=250), nullable=False)
    session_id = Column(String(length=250), nullable=False)
    reset_token = Column(String(length=250), nullable=False)
