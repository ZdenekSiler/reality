import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import datetime


class Proxy:
    client = MongoClient('localhost', 27017)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    base_url = "https://free-proxy-list.net/"

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def download_proxy(self):
        page = requests.get(self.base_url)
        url_content = BeautifulSoup(page.content, 'html.parser')
        body = url_content.find_all('tbody')
        td_tag = re.compile(r'<td.*?>(.*?)</td>')
        try:
            for t in body:
                ip = [re.search(td_tag, str(tr.find_all('td')[:2][0])).group(1) for tr in t.find_all('tr')]
                port = [re.search(td_tag, str(tr.find_all('td')[:2][1])).group(1) for tr in t.find_all('tr')]
                code = [re.search(td_tag, str(tr.find_all('td')[:3][2])).group(1) for tr in t.find_all('tr')]
                country = [re.search(td_tag, str(tr.find_all('td')[:4][3])).group(1) for tr in t.find_all('tr')]
                anon_type = [re.search(td_tag, str(tr.find_all('td')[:5][4])).group(1) for tr in t.find_all('tr')]
                protocol = [re.search(td_tag, str(tr.find_all('td')[:7][6])).group(1) for tr in t.find_all('tr')]
                proxy_server = [str(i) + ":" + str(j) for i, j in zip(ip, port)]
                proxy_details = list(zip(proxy_server, code, country, anon_type, protocol))

                for proxy_server, c_code, country, anon_type, protocol in proxy_details:
                    try:
                        self.client[self.db][self.collection].insert_one({
                            'eff_ins_dt': self.now,
                            'proxy_ip': proxy_server,
                            'country_code': c_code,
                            'country': country,
                            'proxy_type': anon_type,
                            'https_flag': protocol
                        })
                    except Exception as e:
                        print(e)

        except Exception as e:
            print(e)
