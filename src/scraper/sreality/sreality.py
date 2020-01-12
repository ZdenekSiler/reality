from src.scraper.parser import Parser


class EstateJob(Parser):
    base_url = "https://www.sreality.cz"
    name = 'sreality'

    # do i really need the init method here?
    def __init__(self):
        """
        super() gives you access to methods in a superclass from the subclass that inherits from it.
        """
        super().__init__()

    def scrape_url_list(self, url=base_url):
        session = self.set_session()
        while True:
            try:
                page = session.get(url)
                print(page.content)
                break
            except Exception as e:
                print(e)
                self.set_proxy(session, verify=True)
