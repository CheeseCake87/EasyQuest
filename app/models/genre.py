from . import *


class Genre(db.Model):
    # PriKey
    genre_id = schema.Column(types.Integer, primary_key=True)

    # Data
    genre = schema.Column(types.String(256), nullable=False)
    description = schema.Column(types.String(512), nullable=False)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
