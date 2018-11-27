from decimal import Decimal

from basket import Basket


class Discount:
    """ Base class for all discounts defined in system"""
    def apply(self, basket: Basket, base_price: Decimal):
        raise NotImplementedError

class BuyOneGetOneFreeDiscount(Discount):
    def apply(self, basket: Basket, base_price: Decimal):
        return Decimal(0)

class PercentDiscount(Discount):
    def apply(self, basket: Basket, base_price: Decimal):
        return Decimal(0)
