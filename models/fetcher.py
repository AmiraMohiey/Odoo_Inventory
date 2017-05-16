from lxml import html
import requests


class SouqFetcher:
    def __init__(self, page_url):
        self.page = requests.get(page_url)
        self.tree = html.fromstring(self.page.content)

    def get_title(self):
        try:
            title = self.tree.xpath('//div[contains(@class,"product-title")]/h1')[0].text_content()
        except:
            title = ""
        return title

    def get_price(self):
        pass

    def get_category(self):
        try:
            category = self.tree.xpath('//div[contains(@class,"product-title")]//span/a[2]')[0].text_content()
        except:
            category = ""
        return category

    def get_description(self):
        pass

