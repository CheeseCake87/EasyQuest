from . import *


class Quest(db.Model):
    # PriKey
    quest_id = schema.Column(types.Integer, primary_key=True)

    # ForKey
    fk_genre_id = forkey("genre.genre_id")

    # Data
    title = schema.Column(types.String(256), nullable=False)
    summary = schema.Column(types.String(256), nullable=False)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
