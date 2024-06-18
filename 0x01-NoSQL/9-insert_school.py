#!/usr/bin/env python3
""" 9-insert_school"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in the collection based on kwargs
    """
    if not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
