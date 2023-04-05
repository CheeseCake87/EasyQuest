from . import *
from .__mixins__ import CrudMixin


class User(db.Model, CrudMixin):
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
    # 10 = admin
    user_type = schema.Column(types.Integer, nullable=True)

    # Tracking
    created = schema.Column(types.DateTime, default=dater())
    deleted = schema.Column(types.Boolean, default=False)
