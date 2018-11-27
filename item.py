from collections import namedtuple

from flask import current_app

ItemRecord = namedtuple('ItemRecord', ['id', 'price', 'quantity'])


class ProductsStore:
    """
    Naive store class that models products database abstraction.
    It uses flask app context internally for runtime storage.
    """
    def __init__(self):
        if not getattr(current_app, 'product_items', False):
            current_app.product_items = {}

    def get(self, product_id, product_attr=None):
        item = current_app.product_items.get(product_id)
        if product_attr and item:
            return getattr(item, product_attr, None)
        else:
            return item

    def add(self, product_id, data):
        current_app.product_items[product_id] = data

    def delete(self, product_id):
        if product_id in current_app.product_items:
            del current_app.product_items[product_id]



