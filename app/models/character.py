from . import *
from .__mixins__ import CrudMixin


class Character(db.Model, CrudMixin):
    # PriKey
    character_id = schema.Column(types.Integer, primary_key=True)

    # ForKey
    fk_user_id = forkey("user.user_id")
    fk_quest_id = forkey("quest.quest_id")

    # Data
    full_name = schema.Column(types.String(256), nullable=False)
    gender = schema.Column(types.String(256), nullable=False)
    back_story = schema.Column(types.String(1024), nullable=False)
    display_picture = schema.Column(types.String(256), nullable=False)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
