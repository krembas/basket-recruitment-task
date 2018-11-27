from basket import Basket


class Discount:
    """ Base class for all discounts defined in system"""
    def apply(self, basket: Basket):
        raise NotImplementedError

class BuyOneGetOneFreeDiscount(Discount):
    ...

class PercentDiscount(Discount):
    ...
