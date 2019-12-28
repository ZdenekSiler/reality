import datetime
from src.proxy.proxy import Proxy
from src.logging.logger import Log
import logging
from src.mongo.query import Query


class Facade:

    def __init__(self):
        self.proxy = Proxy('proxy', 'proxies')
        self.proxy_query = Query('proxy', 'proxies')

    @staticmethod
    def setup_logging():
        log = Log('log')
        log.setup_logging()


    def prepare_proxy(self):
        self.proxy_query.drop_collection()
        self.proxy.get_proxy_ip()


class Parser:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    def __init__(self, url, name):  # , url, name, search_url):
        self.url = url
        self.name = name


def main():
    facade = Facade()
    facade.setup_logging()
    logger.info('Start')
    facade.prepare_proxy()
    logger.info('Finish')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    main()
