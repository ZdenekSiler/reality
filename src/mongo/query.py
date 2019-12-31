from pymongo import MongoClient
import json
import logging


class Query:
    client = MongoClient('localhost', 27017)
    qry_path = 'mongo/qry_templates/'
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

    def sample_q(self):
        qry_template = 'sample_proxy_case.json'
        qry = self.qry_path + qry_template
        q = self.load_mng_query(qry)

        try:
            for query in self.client[self.db][self.collection].aggregate(q):

                self.logger.info(f"Sample qry:{query}")
                proxies = query['https_flag'] + '://' + str(query['proxy_ip'])

        except Exception as e:
            print(e)
            self.logger.error(f"Error in Sample qry:{e}")
        return proxies
