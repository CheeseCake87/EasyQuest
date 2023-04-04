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
        add_result = bigapp.model("Genre").create(
            batch=[
                {"genre": "Action"},
                {"genre": "Horror"},
                {"genre": "Adventure"},
                {"genre": "Comedy"},
                {"genre": "Crime"},
                {"genre": "Drama"},
                {"genre": "Fantasy"},
                {"genre": "Historical"},
            ]
        )
        # result = bigapp.model("Genre").create(
        #     genre="Horror",
        # )
        print("add_result")
        print(add_result)

        view_result = bigapp.model("Genre").read(id_=1)
        print("view_result")
        print(view_result)

        update_result = bigapp.model("Genre").update(
            field=("genre", "Horror"), values={"description": "Horror"}, return_updated=True
        )
        print("update_result")
        print(update_result)

        delete_result = bigapp.model("Genre").delete(id_=1, return_deleted=True)
        print("delete_result")
        print(delete_result)

    return app
