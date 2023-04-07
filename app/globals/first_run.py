def first_run(db, bigapp, auth):
    db.drop_all()
    db.create_all()
    bigapp.model("Genre").create(
        batch=[
            {"genre": "Mythical Historic Fantasy", "description": "Swords, shields, bows and magic"},
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

    default_admin_email_address = "admin@sys.tem"
    default_admin_password = "password"
    passport = auth.generate_numeric_validator(6)
    salt = auth.generate_salt()
    password = auth.sha_password(default_admin_password, salt)

    bigapp.model("User").create(
        fields={
            "first_name": "Admin",
            "email_address": default_admin_email_address,
            "password": password,
            "salt": salt,
            "passport": passport,
            "user_type": 10,
        }
    )
