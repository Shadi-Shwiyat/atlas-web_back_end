#!/usr/bin/env python3
'''MongoDB python scripting for practice'''
import pymongo


def list_all(mongo_collection) -> list:
    '''Returns a list of all docs
        in a mongodb collection'''
    return list(mongo_collection.find())