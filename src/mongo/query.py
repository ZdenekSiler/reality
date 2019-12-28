from pymongo import MongoClient
import logging
from src.decorator.log_decorators import LogDecorator


class Query:
    # class attribute - the same for all queries
    client = MongoClient('localhost', 27017)
    query_logger = logging.getLogger('query_log')

    """
    INPUT: database_name, collection_na,e
    OUTPUT: Initializer - object instances
    DESCRIPTION: Initialize object with ATTR db_name, collection_name 
    """

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    """
    INPUT : Based on class initializer
    OUTPUT: Drop of collection
    DESCRIPTION: To drop MongodDB collection based on class instance
    """

    @LogDecorator()
    def drop_collection(self):
        self.client[self.db][self.collection].drop()
