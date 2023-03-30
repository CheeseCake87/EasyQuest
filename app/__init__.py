from flask import Flask
from flask_bigapp import BigApp
from flask_sqlalchemy import SQLAlchemy

bigapp = BigApp()
db = SQLAlchemy()


def create_app():
    app = Flask(
        __name__,
        static_folder="global/static",
        static_url_path="/global/static"
    )
    bigapp.init_app(app)
    db.init_app(app)

    return app
