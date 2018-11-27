from flask import Flask, jsonify, session

from basket import Basket


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.secret_key = 'secretk@y'

    @app.route('/basket', methods=['GET'])
    def get_items():
        """Get list of basket items"""
        basket = Basket(session)
        return jsonify()

    @app.route('/basket', methods=['PUT'])
    def update_items():
        basket = Basket(session)
        """Updates (add/remove) basket items"""
        return jsonify()

    @app.route('/basket', methods=['DELETE'])
    def empty():
        basket = Basket(session)
        """Make basket empty"""
        return jsonify()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()