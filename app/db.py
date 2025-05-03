from pymongo import MongoClient

from .config import (
    MONGO_URI,
    MONGO_USERNAME,
    MONGO_PASSWORD,
    MONGO_DATABASE,
    MONGO_COLLECTION
)


def get_collection():
    client = MongoClient(
        MONGO_URI,
        username=MONGO_USERNAME,
        password=MONGO_PASSWORD
    )
    db = client[MONGO_DATABASE]
    collection = db[MONGO_COLLECTION]
    return collection