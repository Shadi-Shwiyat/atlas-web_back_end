#!/usr/bin/env python3
'''MongoDB python scripting for practice'''
import pymongo


def schools_by_topic(mongo_collection, topic) -> list:
    '''Returns the list of school having a specific topic'''
    results = mongo_collection.find({'topics': [topic]})
    return list(results)
