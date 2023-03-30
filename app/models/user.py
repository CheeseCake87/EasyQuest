from . import *


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
