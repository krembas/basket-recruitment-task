from decimal import Decimal

from flask import Flask, jsonify, session, request, abort, Response

from basket import Basket
from discounts import BuyOneGetOneFreeDiscount, PercentDiscount
from item import ProductsStore, ItemRecord


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.secret_key = 'secretk@y'

    # build products "database" that keeps all available products (its data;)
    with app.app_context():
        s = ProductsStore()
        s.add('1', ItemRecord(id='1', price='1.23', quantity=11))
        s.add('2', ItemRecord(id='2', price='3.21', quantity=11)),
        s.add('3', ItemRecord(id='3', price='20.0', quantity=11)),
        s.add('4', ItemRecord(id='4', price='20.1', quantity=11))

    # setup all supported discounts
    app.discounts = (
        BuyOneGetOneFreeDiscount(),
        PercentDiscount(),
    )


    @app.route('/basket', methods=['GET'])
    def get_items():
        """Get list of basket items"""
        basket = Basket(session)
        return jsonify({'items': [{'id': id, 'qty': qty} for id, qty in basket.items()]})

    @app.route('/basket', methods=['PUT'])
    def update_items():
        """Updates (add/remove) basket items"""
        if not request.json:
            abort(400)
        basket = Basket(session)
        items = [ItemRecord(id=item['id'],
                            quantity=int(item['qty']),
                            price=None) for item in request.json['items']]
        basket.update_items(items)
        return Response(status=200)

    @app.route('/basket', methods=['DELETE'])
    def empty():
        basket = Basket(session)
        basket.empty()
        """Make basket empty"""
        return Response(status=204)

    @app.route('/basket/account')
    def account():
        basket = Basket(session)

        # calculate total discount for products in basket
        total_discount = 0
        basket_price = base_price = basket.items_sum_price()
        for dsc in app.discounts:
            discount = dsc.apply(basket, base_price)
            base_price -= discount
            total_discount += discount

        total_price = Decimal(basket_price) - Decimal(total_discount)

        return jsonify({'total_price': str(total_price.quantize(Decimal('.01')))})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
