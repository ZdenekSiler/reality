import requests as req
from bs4 import BeautifulSoup
from pymongo import MongoClient
import logging
import random
from src.mongo.query import Query


class UserAgent:
    client = MongoClient('localhost', 27017)
    logger = logging.getLogger(__name__)
    url = 'http://www.useragentstring.com/pages/useragentstring.php?name='
    brs = ['Firefox', 'Internet+Explorer', 'Opera', 'Safari', 'Edge', 'Googlebot', 'YahooSeeker', 'Netscape', 'Chimera',
           'Googlebot', 'YahooSeeker', 'SeznamBot']

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection
        self.query_ua = Query('ua', 'user_agent')

    def get_ua(self):
        for br in self.brs:
            url = 'http://www.useragentstring.com/pages/useragentstring.php?name=' + br
            r = req.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')
            else:
                soup = False

            if soup:
                div = soup.find('div', {'id': 'liste'})

                for el in div:
                    for li in el.findAll('li'):
                        try:
                            self.client[self.db][self.collection].insert_one({"browser": br, self.collection: li.text})
                            self.logger.info(f'browser: {li.text}')
                        except Exception as e:
                            self.logger.error(e)

    def set_ua(self):
        uas = self.query_ua.get_selected_col('user_agent')
        user_agent = random.choice(uas)
        self.logger.info(f"User Agent:{user_agent}, {type(user_agent)}")
        return user_agent
