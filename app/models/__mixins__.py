from . import db
from . import insert, update, delete, select


class CrudMixin:
    id_field: str

    @classmethod
    def create(
            cls,
            fields: dict = None,
            batch: list[dict] = None
    ):
        if batch is not None:
            result = db.session.scalars(
                insert(cls).returning(cls),
                batch
            )
            db.session.commit()
            return result.all()

        result = db.session.scalar(
            insert(cls).returning(cls).values(**fields)
        )
        db.session.commit()
        return result

    @classmethod
    def read(
            cls,
            id_: int = None,
            field: tuple = None,
            fields: dict = None,
            _updating: bool = False,
            _deleting: bool = False
    ):
        if _updating:
            base_query = update(cls)
        elif _deleting:
            base_query = delete(cls)
        else:
            base_query = select(cls)

        if id_ is not None:
            kwargs = {cls.id_field: id_}
            base_query = base_query.filter_by(**kwargs)
            if _updating or _deleting:
                return base_query
            return db.session.scalars(base_query).one_or_none()

        if field is not None:
            base_query = base_query.filter_by(**{field[0]: field[1]})
            if _updating or _deleting:
                return base_query
            return db.session.scalars(base_query).all()

        if fields is not None:
            base_query = base_query.filter_by(**fields)
            if _updating or _deleting:
                return base_query
            return db.session.scalars(base_query).all()

    @classmethod
    def update(
            cls,
            id_: int = None,
            field: tuple = None,
            fields: dict = None,
            values: dict = None,
            return_updated: bool = False
    ):
        query = cls.read(id_=id_, field=field, fields=fields, _updating=True).values(values)
        if return_updated:
            result = db.session.execute(query.returning(cls)).scalars().all()
            db.session.commit()
            return result
        db.session.execute(query)
        return True

    @classmethod
    def delete(
            cls,
            id_: int = None,
            field: tuple = None,
            fields: dict = None,
            return_deleted: bool = False
    ):
        query = cls.read(id_=id_, field=field, fields=fields, _deleting=True)
        if return_deleted:
            result = db.session.execute(query.returning(cls)).scalars().all()
            db.session.commit()
            return result
        db.session.execute(query)
        db.session.commit()
        return True