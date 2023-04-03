from flask import Flask
from flask_bigapp import BigApp
from flask_sqlalchemy import SQLAlchemy

bigapp = BigApp()
db = SQLAlchemy()


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
        static_url_path="/static"
    )
    bigapp.init_app(app)
    db.init_app(app)

    bigapp.import_builtins()
    bigapp.import_models(from_folder="models")
    bigapp.import_blueprints("blueprints")

    with app.app_context():
        db.drop_all()
        db.create_all()
        # result = bigapp.model("Genre").create(
        #     batch=[
        #         {"genre": "Action"},
        #         {"genre": "Adventure"},
        #         {"genre": "Comedy"},
        #         {"genre": "Crime"},
        #         {"genre": "Drama"},
        #         {"genre": "Fantasy"},
        #         {"genre": "Historical"},
        #     ]
        # )
        result = bigapp.model("Genre").create(
            genre="Horror",
        )
        print(result)

    return app
