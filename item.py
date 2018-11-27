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

    def get(self, product_id):
        ...

    def add(self, product_id, item: ItemRecord):
        ...

    def delete(self, product_id):
        ...



