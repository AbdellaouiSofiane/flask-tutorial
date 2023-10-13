import json
import os

from flask import Flask


def create_app():

    # Init flask app
    app = Flask(__name__)

    # Config app
    app.config.from_mapping(SECRET_KEY="Dummy-Secret-KEY")

    # Register index route
    @app.route('/')
    def hello():
        response = json.dumps({"message": "I'm alive !!"})
        return response, 200, {'Content-Type': 'application/json'}

    return app
