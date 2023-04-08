from . import *
from .__mixins__ import CrudMixin


class Character(db.Model, CrudMixin):
    id_field = "character_id"

    # PriKey
    character_id = schema.Column(types.Integer, primary_key=True)

    # ForKey
    fk_user_id = forkey("user.user_id")
    fk_quest_id = forkey("quest.quest_id")

    # Protection
    locked = schema.Column(types.Boolean, nullable=False, default=False)
    approved = schema.Column(types.Boolean, nullable=False, default=False)

    # Data
    full_name = schema.Column(types.String(256), nullable=False)
    back_story = schema.Column(types.String(1024), nullable=False)
    display_picture = schema.Column(types.String(256), nullable=True)

    # Vitals
    health = schema.Column(types.Integer, nullable=False, default=100)
    sleeping = schema.Column(types.Boolean, nullable=False, default=False)
    confused = schema.Column(types.Boolean, nullable=False, default=False)
    poisoned = schema.Column(types.Boolean, nullable=False, default=False)
    buffed = schema.Column(types.Boolean, nullable=False, default=False)

    # Arc
    arc_card = schema.Column(types.JSON, nullable=True)
    arc = schema.Column(types.String(256), nullable=True)
    arc_description = schema.Column(types.String(1024), nullable=True)
    arc_modifier = schema.Column(types.String(256), nullable=True)
    arc_bonus = schema.Column(types.String(256), nullable=True)

    # Weapon
    weapon = schema.Column(types.String(256), nullable=True)

    # Attack & Defense
    attack = schema.Column(types.Integer, nullable=False, default=1)
    defense = schema.Column(types.Integer, nullable=False, default=1)

    # Attributes
    strength = schema.Column(types.Integer, nullable=False, default=1)
    agility = schema.Column(types.Integer, nullable=False, default=1)
    intelligence = schema.Column(types.Integer, nullable=False, default=1)
    luck = schema.Column(types.Integer, nullable=False, default=1)
    perception = schema.Column(types.Integer, nullable=False, default=1)
    persuasion = schema.Column(types.Integer, nullable=False, default=1)

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
