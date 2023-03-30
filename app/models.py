from datetime import datetime
from datetime import timedelta

from pytz import timezone
from sqlalchemy import schema, types

from app import db


def dater(ltz: str = "Europe/London", mask: str = "%Y-%m-%d %H:%M:%S", days_delta: int = 0) -> datetime:
    local_tz = timezone(ltz)
    if days_delta < 0:
        apply_delta = (datetime.now(local_tz) - timedelta(days=abs(days_delta))).strftime(mask)
        return datetime.strptime(apply_delta, mask)
    if days_delta > 0:
        apply_delta = (datetime.now(local_tz) + timedelta(days=days_delta)).strftime(mask)
        return datetime.strptime(apply_delta, mask)
    return datetime.strptime(datetime.now(local_tz).strftime(mask), mask)


def forkey(table_dot_field: str) -> schema.Column:
    return schema.Column(types.Integer, schema.ForeignKey(table_dot_field), nullable=False)


class User(db.Model):
    # PriKey
    user_id = schema.Column(types.Integer, primary_key=True)

    # Data
    username = schema.Column(types.String(256), nullable=False)
    password = schema.Column(types.String(512), nullable=False)
    salt = schema.Column(types.String(4), nullable=False)
    disabled = schema.Column(db.Boolean, default=False)

    # Permissions
    # 10 = admin, 3 = manager, 2 = drafter, 1 = sales
    user_type = schema.Column(types.Integer, nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
    deleted = schema.Column(types.Boolean, default=False)


class Genre(db.Model):
    # PriKey
    genre_id = schema.Column(types.Integer, primary_key=True)

    # Data
    genre = schema.Column(types.String(256), nullable=False)
    description = schema.Column(types.String(512), nullable=False)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())


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


class Character(db.Model):
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
