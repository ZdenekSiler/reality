from src.scraper.parser import Parser
import logging
import json
import itertools
from selenium import webdriver

class EstateJob(Parser):
    base_url = "https://www.sreality.cz/hledani/prodej/"
    name = 'sreality'
    #items = ['byty','domy','projekty','pozemky','komercni','ostatni']
    items = ['domy']
    logger = logging.getLogger(__name__)

    # do i really need the init method here?
    def __init__(self):
        """
        super() gives you access to methods in a superclass from the subclass that inherits from it.
        """
        super().__init__()

    def get_district(self):
        dist = []
        with open ('filter/regions.json','r') as r:
            regions = json.loads(r.read())
            r = [region for region in regions['region']]
        # for districts in r:
        #     dist.append(regions['region'][districts])
        #return [dist]
        dist.append(regions['region']['stredocesky'])
        dist.append(regions['region']['praha'])
        #return [[item for dist in l for item in dist]
        return list(itertools.chain(*dist))

    def get_url(self):
        url_dict = []
        for district in self.get_district():
            url = self.base_url
            for item in self.items:
                url_dict.append(url + item + '/' + district)
            self.logger.info(url)
        return url_dict

    def scrape_url_list(self):
        session = self.set_session()
        self.logger.info(f'Session headers: {session.headers}')
        while True:
            try:
                break
            except Exception as e:
                self.set_proxy(session, verify=True)
                self.logger.error(e)

    def web_driver_scraper(self):
        url = 'https://www.sreality.cz/hledani/prodej/domy/praha-vychod,praha-zapad?navic=nizkoenergeticky&cena-od=0&cena-do=9000000'
        browser = webdriver.Chrome()
        browser.get(url)
        locality = []
        nm = []
        price = []
        for pl in browser.find_elements_by_xpath("//div[@class='content']"):
            for loc in pl.find_elements_by_xpath("//span[@class='locality ng-binding']"):
                locality.append(loc.text)
            for name in pl.find_elements_by_xpath("//span[@class='name ng-binding']"):
                nm.append(name.text)
            for prc in pl.find_elements_by_xpath("//span[@class='norm-price ng-binding']"):
                price.append(prc.text)

        li = list(zip(locality,nm,price))
        print(li)
            
estate = EstateJob()
estate.web_driver_scraper()