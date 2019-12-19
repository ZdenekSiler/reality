import datetime
from src.proxy.proxy import Proxy


class Facade:

    def __init__(self):
        self.proxy = Proxy('proxy', 'proxies')

    def prepare_proxy(self):
        self.proxy.download_proxy()


class Parser:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    def __init__(self, url, name):  # , url, name, search_url):
        self.url = url
        self.name = name


def main():
    facade = Facade()
    facade.prepare_proxy()


if __name__ == '__main__':
    main()
