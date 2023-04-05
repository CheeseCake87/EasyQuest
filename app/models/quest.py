from . import *
from .__mixins__ import CrudMixin


class Quest(db.Model, CrudMixin):
    id_field = "quest_id"

    # PriKey
    quest_id = schema.Column(types.Integer, primary_key=True)

    # ForKey
    fk_genre_id = forkey("genre.genre_id")

    # Data
    title = schema.Column(types.String(256), nullable=False)
    summary = schema.Column(types.String(256), nullable=False)
    live = schema.Column(types.Boolean, default=False)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())

    # Relationships
    rel_genre = relationship(
        "Genre",
        primaryjoin="Genre.genre_id==Quest.fk_genre_id",
        back_populates="rel_quests"
    )
