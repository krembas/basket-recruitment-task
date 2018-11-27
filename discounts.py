from decimal import Decimal
from typing import Tuple

from basket import Basket
from item import ProductsStore


class Discount:
    """ Base class for all discounts defined in system"""
    def apply(self, basket: Basket, base_price: Decimal):
        raise NotImplementedError


class BuyOneGetOneFreeDiscount(Discount):
    def __init__(self, discounted_items_ids: Tuple):
        self._discounted_items_ids = discounted_items_ids

    def apply(self, basket: Basket, base_price: Decimal):
        discount = 0
        s = ProductsStore()
        for item_id in basket:
            if item_id in self._discounted_items_ids:
                discount += Decimal(s.get(item_id, 'price')) * (basket[item_id] // 2)
        return discount


class PercentDiscount(Discount):
    def apply(self, basket: Basket, base_price: Decimal):
        return Decimal(0)
