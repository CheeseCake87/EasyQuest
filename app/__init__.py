from pathlib import Path

from app.extensions import *
from app.globals.first_run import first_run


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
        static_url_path="/static"
    )

    sysconf_location = Path(Path(app.root_path) / "sysconf.ini")
    sysconf.read(Path(sysconf_location))

    bigapp.init_app(app)
    db.init_app(app)

    bigapp.import_builtins()
    bigapp.import_models(from_folder="models")
    bigapp.import_blueprints("blueprints")

    with app.app_context():
        if sysconf.getboolean("SYSTEM", "FIRST_RUN"):
            print("First run detected, creating database...")
            sysconf.set("SYSTEM", "FIRST_RUN", "false")
            with open(sysconf_location, "w") as f:
                sysconf.write(f)

            first_run(db, bigapp, auth)

    @app.before_request
    def before_request():
        bigapp.init_session()

    @app.after_request
    def after_request(response):
        return response

    return app
