from odoo import models, fields
from lxml import html
import requests
from fetcher import SouqFetcher


class Product(models.Model):
    def fetch_data(self):
        scrapper = SouqFetcher(self.url)
        title = scrapper.get_title()
        if title != "":
            self.title = title
            #self.price = scrapper.get_price()
            self.category = scrapper.get_category()
            #self.description = scrapper.get_description()
            self.numberOfUpdates = self.numberOfUpdates + 1

    _name = 'souq_scrapper.products'

    url = fields.Char(string='Souq URL')
    title = fields.Char(string='Product Title')
    category = fields.Char(string='Category')
    description = fields.Char(string='Description')
    price = fields.Float(string='Price')

    image = fields.Binary()

    numberOfUpdates = fields.Integer('Number of updates')
