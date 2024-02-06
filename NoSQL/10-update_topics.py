#!/usr/bin/env python3
'''MongoDB python scripting for practice'''
import pymongo


def update_topics(mongo_collection, name, topics) -> None:
    '''Changes all topics of a school
        document based on the name'''
    filter_query = {'name': name}
    update_query = {'$set': {'topics': topics}}
    mongo_collection.update_many(filter_query, update_query)
