from app.extensions import bigapp


def loader(app):
    @app.before_request
    def before_request():
        bigapp.init_session()
