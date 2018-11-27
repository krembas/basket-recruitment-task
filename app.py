from flask import Flask, jsonify


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.secret_key = 'secretk@y'

    @app.route('/basket', methods=['GET'])
    def get_items():
        """Get list of basket items"""
        return jsonify()

    @app.route('/basket', methods=['PUT'])
    def update_items():
        """Updates (add/remove) basket items"""
        return jsonify()

    @app.route('/basket', methods=['DELETE'])
    def empty():
        """Make basket empty"""
        return jsonify()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()