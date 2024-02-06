#!/usr/bin/env python3
'''MongoDB python scripting for practice'''
import pymongo


def insert_school(mongo_collection, **kwargs) -> int:
    '''Inserts a new document in a
        collection based on kwargs'''
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
