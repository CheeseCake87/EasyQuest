def loader(app):
    @app.get("/robots.txt")
    def robots():
        return app.send_static_file("robots.txt")
