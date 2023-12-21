def loader(app):
    @app.cli.command("add-admin")
    def cli_add_admin():
        """Add an admin user"""
        from app.models.user import User

        if User.exists("admin@system"):
            print("Admin user already exists")
            return

        User.add_user(
            first_name="Admin",
            email_address="admin@system",
            password="admin",
            permission_level=10,
        )

        print("Admin user created")
