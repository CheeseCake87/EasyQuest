from . import *
from .__mixins__ import CrudMixin


class Genre(db.Model, CrudMixin):
    id_field = "genre_id"

    # PriKey
    genre_id = schema.Column(types.Integer, primary_key=True)

    # Data
    genre = schema.Column(types.String(256), nullable=False)
    description = schema.Column(types.String(512), nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
