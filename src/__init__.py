from src.proxy.proxy import Proxy
from src.logging.logger import Log
import logging
from src.mongo.query import Query
from src.scraper.parser import Parser
#from src.scraper.sreality.sreality import EstateJob
from src.ua.user_agent import UserAgent


class Facade:

    def __init__(self):
        self.proxy = Proxy('proxy', 'proxies')
        self.proxy_query = Query('proxy', 'proxies')
        self.ua_query = Query('ua', 'user_agent')
        self.parser = Parser()
        self.ua = UserAgent('ua', 'user_agent')
        #self.estate = EstateJob()

    def prepare_proxy(self):
        self.proxy_query.drop_collection()
        self.proxy.get_proxy_ip()

    def prepare_ua(self):
        self.ua_query.drop_collection()
        self.ua.get_ua()

    def estate(self):
        self.estate.scrape_url_list()


def setup_logging():
    log = Log('log')
    log.setup_logging()


def main():
    facade = Facade()
    setup_logging()
    logger.info('Start')
    facade.prepare_proxy()
    facade.prepare_ua()
    #facade.estate.scrape_url_list()
    logger.info('Finish')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    main()
