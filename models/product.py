from odoo import models, fields
from lxml import html
import requests

class Product(models.Model):
    _name = 'souq_scrapper.products'

    url = fields.Char(string='product url')
    name = fields.Char(string='Product')
    category = fields.Char(string='Category')
    description = fields.Char(string='Description')
    title = fields.Char(string='Title')
    price = fields.Float(string='Price')
    image = fields.Binary()
    numberOfUpdates = fields.Integer('Number of updates')
