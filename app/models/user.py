from app.extensions import auth
from flask_bigapp.orm import CrudMixin
from . import *


class User(db.Model, CrudMixin):
    __id_field__ = 'user_id'
    __session__ = db.session

    # PriKey
    user_id = schema.Column(types.Integer, primary_key=True)

    # Data
    first_name = schema.Column(types.String(128), nullable=True)
    email_address = schema.Column(types.String(512), nullable=False)
    password = schema.Column(types.String(512), nullable=False)
    salt = schema.Column(types.String(4), nullable=False)
    uuid = schema.Column(types.String(256), nullable=False)
    disabled = schema.Column(db.Boolean, default=False)

    # Permissions
    # 10 = admin, 1 = user
    permission_level = schema.Column(types.Integer, nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
    deleted = schema.Column(types.Boolean, default=False)

    # Relationships
    rel_characters = relationship(
        "Character",
        primaryjoin="Character.fk_user_id==User.user_id",
        back_populates="rel_user"
    )

    @classmethod
    def login(cls, email_address, password):
        if email_address is None or password is None:
            return False
        user = cls.read(fields={'email_address': email_address}, _auto_output=False).first()
        if user:
            if auth.auth_password(password, user.password, user.salt):
                return user
        return None

    @classmethod
    def exists(cls, email_address):
        return cls.read(fields={'email_address': email_address}, _auto_output=False).one_or_none() is not None

    @classmethod
    def enable(cls, user_id):
        cls.update(id_=user_id, values={'disabled': False})
        return

    @classmethod
    def disable(cls, user_id):
        cls.update(id_=user_id, values={'disabled': True})
        return

    @classmethod
    def add_user(cls, first_name, email_address, password, permission_level=1):
        salt = auth.generate_salt()
        return cls.create(
            values={
                'first_name': first_name,
                'email_address': email_address,
                'password': auth.hash_password(password, salt),
                'salt': salt,
                'permission_level': permission_level,
                'uuid': auth.generate_private_key(email_address)
            }
        )
