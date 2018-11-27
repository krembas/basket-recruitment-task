from flask import Flask, jsonify, session, request, abort, Response

from basket import Basket
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

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()