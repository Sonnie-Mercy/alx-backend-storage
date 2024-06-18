#!/usr/bin/env python3
""" lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
