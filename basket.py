from collections import Counter


class Basket(Counter):
    """
    Covers core basket functionality.

    Basket must do three things, but do well ;)
    1) update (add/delete) items from it
    2) get items list (basket content)
    3) empty itself

    Counter is a great "framework" for this as it covera all that actions by default :)
    """
    def __init__(self, session, *args, **kwargs):
        try:
            self.update(**session['basket'])
        except KeyError:
            super().__init__(*args, **kwargs)
        session['basket'] = self

    def get_items(self):
        ...

    def update_items(self):
        ...

    def empty(self):
        ...
