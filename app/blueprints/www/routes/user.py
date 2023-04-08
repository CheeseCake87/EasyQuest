from flask import redirect, url_for, session

from app.models.user import User
from .. import bp


@bp.get("/enable/user/<user_id>")
def enable_user(user_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    User.enable(user_id)
    return redirect(url_for('www.users'))


@bp.get("/disable/user/<user_id>")
def disable_user(user_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    User.disable(user_id)
    return redirect(url_for('www.users'))