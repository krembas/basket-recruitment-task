from flask import Flask


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.secret_key = 'secretk@y'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()