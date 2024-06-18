#!/usr/bin/env python3
"""12-log_stats.py"""
from pymongo import MongoClient


def log_stats():
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    client = MngoClient('mongodb://127.0.0.1:27017/')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("MEthods:")
    for methods in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    st_chk = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{st_chk} status check")


if __name__ == "__main__":
    log_stats()
