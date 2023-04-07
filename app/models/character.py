from . import *
from .__mixins__ import CrudMixin


class Character(db.Model, CrudMixin):
    id_field = "character_id"

    # PriKey
    character_id = schema.Column(types.Integer, primary_key=True)

    # ForKey
    fk_user_id = forkey("user.user_id")
    fk_quest_id = forkey("quest.quest_id")

    # Data
    full_name = schema.Column(types.String(256), nullable=False)
    back_story = schema.Column(types.String(1024), nullable=False)
    display_picture = schema.Column(types.String(256), nullable=True)
    arc = schema.Column(types.String(256), nullable=True)
    arc_card = schema.Column(types.JSON, nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())

    # Relationships
    rel_user = relationship(
        "User",
        back_populates="rel_characters"
    )

    rel_quest = relationship(
        "Quest",
        back_populates="rel_characters"
    )
