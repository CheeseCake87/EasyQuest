from . import *


class Quest(db.Model):
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

    @classmethod
    def create(cls, title, summary, genre_id):
        _create = insert(cls).values(
            title=title,
            summary=summary,
            fk_genre_id=genre_id
        )
        db.session.add(_create)
        db.session.commit()
        return _create

    @classmethod
    def update(cls, quest_id, title, summary, genre_id):
        _update = update(
            cls
        ).where(
            cls.quest_id == quest_id
        ).values(
            title=title,
            summary=summary,
            fk_genre_id=genre_id
        )
        result = db.session.execute(_update)
        db.session.commit()
        return result

    @classmethod
    def get(cls, quest_id):
        _get = select(cls).where(cls.quest_id == quest_id)
        result = db.session.execute(_get).scalar_one_or_none()
        return result

    @classmethod
    def get_all(cls):
        return cls.query.all()
