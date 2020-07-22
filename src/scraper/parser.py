import datetime
from src.mongo.query import Query
from urllib.parse import urlparse
import requests
import logging
from src.ua.user_agent import UserAgent


class Parser:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    def __init__(self):
        self.proxy_query = Query('proxy', 'proxies')
        self.ua = UserAgent('ua', 'user_agent')
        self.logger = logging.getLogger(__name__)

    def set_proxy(self, session, verify=False):
        proxy = self.proxy_query.sample_q
        self.logger.info(f'proxy_server: {proxy}')
        session.proxies = {urlparse(proxy).scheme: proxy}

        if not verify:
            return  # end up the function if the condition is met
        try:
            stat_cd = str(session.get('https://httpbin.org/ip').status_code)
            self.logger.info(f"Session status code:{stat_cd}")
            return
        except Exception as e:
            self.logger.info(f'Connection error :{e}')

    def set_session(self):
        user_agent = self.ua.set_ua()
        session = requests.Session()
        session.headers = {"User-agent": user_agent}
        self.set_proxy(session, verify=False)
        return session
