from . import db
from . import insert, update, delete, select, asc, desc


class CrudMixin:
    id_field: str

    @classmethod
    def create(
            cls,
            values: dict = None,
            batch: list[dict] = None,
            wash_attributes: bool = False,
    ):

        if batch is not None:
            new_batch = []
            if wash_attributes:
                for item in batch:
                    for key, value in item.items():
                        if not hasattr(cls, key):
                            del item[key]
                    new_batch.append(item)

            process_batch = batch if not wash_attributes else new_batch
            result = db.session.scalars(
                insert(cls).returning(cls),
                process_batch
            )
            db.session.commit()
            return result.all()

        if wash_attributes:
            for key, value in values.items():
                if not hasattr(cls, key):
                    del values[key]

        result = db.session.scalar(
            insert(cls).returning(cls).values(**values)
        )
        db.session.commit()
        return result

    @classmethod
    def read(
            cls,
            id_: int = None,
            field: tuple = None,
            fields: dict = None,
            all_rows: bool = False,
            order_by: str = None,
            order_desc: bool = False,
            _updating: bool = False,
            _deleting: bool = False,
            _auto_output: bool = True
    ):
        if _updating:
            base_query = update(cls)
        elif _deleting:
            base_query = delete(cls)
        else:
            if order_by is not None:
                column = getattr(cls, order_by)
                if order_desc:
                    base_query = select(cls).order_by(desc(column))
                else:
                    base_query = select(cls).order_by(asc(column))
            else:
                base_query = select(cls)

        if all_rows:
            return db.session.scalars(base_query).all()

        if id_ is not None:
            kwargs = {cls.id_field: id_}
            base_query = base_query.filter_by(**kwargs)
            if _updating or _deleting:
                return base_query
            if _auto_output:
                return db.session.scalars(base_query).one_or_none()
            return db.session.scalars(base_query)

        if field is not None:
            base_query = base_query.filter_by(**{field[0]: field[1]})
            if _updating or _deleting:
                return base_query
            if _auto_output:
                return db.session.scalars(base_query).all()
            return db.session.scalars(base_query)

        if fields is not None:
            base_query = base_query.filter_by(**fields)
            if _updating or _deleting:
                return base_query
            if _auto_output:
                return db.session.scalars(base_query).all()
            return db.session.scalars(base_query)

    @classmethod
    def update(
            cls,
            values: dict,
            id_: int = None,
            field: tuple = None,
            fields: dict = None,
            return_updated: bool = False,
            wash_attributes: bool = False
    ):
        if wash_attributes:
            for key, value in values.items():
                if not hasattr(cls, key):
                    del values[key]
        query = cls.read(id_=id_, field=field, fields=fields, _updating=True).values(values)
        if return_updated:
            result = db.session.execute(query.returning(cls)).scalars().all()
            db.session.commit()
            return result
        db.session.execute(query)
        db.session.commit()
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
            return result[0] if len(result) > 0 else result
        db.session.execute(query)
        db.session.commit()
        return True
