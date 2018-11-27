from collections import Counter
from typing import List

from item import ItemRecord


class Basket(Counter):
    """
    Covers core basket functionality.

    Basket must do three things, but do well ;)
    1) update (add/delete) items from it
    2) get items list (basket content)
    3) empty itself

    Counter is a great "framework" for this as it covers all that actions by default :)
    """
    def __init__(self, session, *args, **kwargs):
        try:
            self.update(**session['basket'])
        except KeyError:
            super().__init__(*args, **kwargs)
        session['basket'] = self

    def _clean(self):
        """
        Clean rubbish basket items (with zero or negative amount values) that may
        be produced as a result of Counter's update() / subtract() methods
        :return:
        """

        crap_items =[]
        for item in self:
            if self[item] <= 0:
                crap_items.append(item)
        for item in crap_items:
                del self[item]

    def get_items(self, items: List[ItemRecord]):
        return self

    def update_items(self, items: List[ItemRecord]):
        for item in items:
            self.update({item.id: item.quantity})
        self._clean()

    def empty(self):
        self.clear()

