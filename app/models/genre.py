from . import *


class Genre(db.Model):
    # PriKey
    genre_id = schema.Column(types.Integer, primary_key=True)

    # Data
    genre = schema.Column(types.String(256), nullable=False)
    description = schema.Column(types.String(512), nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())

    @classmethod
    def create(cls, genre: str = None, description: str = None, batch: list[dict] = None):
        if batch is not None:
            result = db.session.scalars(
                insert(cls).returning(cls),
                batch
            )
            db.session.commit()
            return result.all()

        result = db.session.scalar(
            insert(cls).returning(cls).values(
                genre=genre,
                description=description
            )
        )
        db.session.commit()
        return result
