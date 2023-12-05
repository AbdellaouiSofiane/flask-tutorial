import os

from flask import Flask


def create_app():

    # Init flask app
    app = Flask(__name__, instance_relative_config=True)

    # Config app
    app.config.from_mapping(
        SECRET_KEY="Dummy-Secret-KEY",
        DATABASE=os.path.join(app.instance_path, "database.sqlite"))

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register index route
    @app.route('/')
    def hello():
        return {"message": "I'm alive !!"}

    # Init database
    from . import db
    db.init_app(app)

    return app
