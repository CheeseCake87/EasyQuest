from pathlib import Path

from app.extensions import *


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

            db.drop_all()
            db.create_all()
            bigapp.model("Genre").create(
                batch=[
                    {"genre": "Mythical Historical Fantasy", "description": "Swords, shields, bows and magic"},
                    {"genre": "Cult Mystery", "description": "Cults, mysteries and conspiracies"},
                    {"genre": "Zombie Apocalypse", "description": "Zombies, bandits and looting"},
                    {"genre": "Apocalypse", "description": "Bandits and looting"},
                    {"genre": "Crime Film Noir", "description": "Smoke and back alleys, see!"},
                    {"genre": "Existential Horror", "description": "Your existence means nothing."},
                    {"genre": "Dystopian Future", "description": "The future is bleak"},
                    {"genre": "Mythic Folklore", "description": "Werewolves, vampires, ghosts and other monsters"},
                    {"genre": "Science Fiction", "description": "Aliens, robots, space travel and other cool stuff"},
                ]
            )

            default_admin_email_address = "admin@users.system"
            default_admin_password = "adminpassword"
            passport = auth.generate_numeric_validator(6)
            salt = auth.generate_salt()
            password = auth.sha_password(default_admin_password, salt)

            bigapp.model("User").create(
                fields={
                    "email_address": default_admin_email_address,
                    "password": password,
                    "salt": salt,
                    "passport": passport,
                    "user_type": 10,
                }
            )

    return app
