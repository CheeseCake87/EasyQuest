from app.extensions import auth
from . import *
from .__mixins__ import CrudMixin


class User(db.Model, CrudMixin):
    id_field = 'user_id'

    # PriKey
    user_id = schema.Column(types.Integer, primary_key=True)

    # Data
    first_name = schema.Column(types.String(128), nullable=True)
    email_address = schema.Column(types.String(512), nullable=False)
    password = schema.Column(types.String(512), nullable=False)
    salt = schema.Column(types.String(4), nullable=False)
    passport = schema.Column(types.Integer, nullable=False)
    disabled = schema.Column(db.Boolean, default=False)

    # Permissions
    # 10 = admin, 1 = user
    user_type = schema.Column(types.Integer, nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
    deleted = schema.Column(types.Boolean, default=False)

    @classmethod
    def login(cls, email_address, password):
        if email_address is None or password is None:
            return False
        user = cls.read(fields={'email_address': email_address}, _auto_output=False).one_or_none()
        if user:
            if auth.auth_password(password, user.password, user.salt):
                return user
        return None

    @classmethod
    def exists(cls, email_address):
        return cls.read(fields={'email_address': email_address}, _auto_output=False).one_or_none() is not None
