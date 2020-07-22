from pymongo import MongoClient
import json
import logging
import os


class Query:
    client = MongoClient('localhost', 27017)
    qry_path = os.path.dirname(os.path.abspath(__file__)) + '/qry_templates/'
    logger = logging.getLogger(__name__)

    """
    INPUT: database_name, collection_na,e
    OUTPUT: Initializer - object instances
    DESCRIPTION: Initialize object with ATTR db_name, collection_name 
    """

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    """
    INPUT: Based on class initializer
    OUTPUT: Drop of collection
    DESCRIPTION: To drop MongoDB collection based on class instance
    """

    def drop_collection(self):
        self.client[self.db][self.collection].drop()
        self.logger.info(f'Deleting: {self.db}.{self.collection}')

    """
    INPUT: Mongo query template in json format
    OUTPUT: Mongo query statement to be executed
    DESCRIPTION: Load a query template from the json object
    """

    @staticmethod
    def load_mng_query(qry):
        with open(qry, 'r') as j:
            q = json.load(j)['qry_stmt']
        return q

    """
    INPUT: No
    OUTPUT: Proxy server ip address
    DESCRIPTION: Get a randomized proxy server ip address 
    """

    @property
    def sample_q(self):
        qry_template = 'sample_proxy_case.json'
        qry = self.qry_path + qry_template
        q = self.load_mng_query(qry)
        proxies = {}
        try:
            for query in self.client[self.db][self.collection].aggregate(q):
                self.logger.info(f"Sample qry:{query}")
                proxies = query['https_flag'] + '://' + str(query['proxy_ip'])

        except Exception as e:
            self.logger.error(f"Error in Sample qry:{e}")
        return proxies

    """
    INPUT: Column name
    OUTPUT: Proxy server ip address
    DESCRIPTION: Projection in MongoDB (SELECT column_name from db.collection) 
    """

    def get_selected_col(self, col):
        ret_val = []
        try:
            for query in self.client[self.db][self.collection].aggregate([{'$project': {col: 1, '_id': 0}}]):
                ret_val.append(query[col])
        except Exception as e:
            self.logger.error(e)
        return ret_val
