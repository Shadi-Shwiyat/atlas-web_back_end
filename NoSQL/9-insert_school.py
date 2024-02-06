#!/usr/bin/env python3
'''MongoDB python scripting for practice'''
import pymongo


def insert_school(mongo_collection, **kwargs) -> list:
    '''Returns a list of all docs
        in a mongodb collection'''
    return list(mongo_collection.find())