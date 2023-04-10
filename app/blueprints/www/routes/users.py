from flask import render_template
from flask_bigapp.security import login_check, permission_check

from app.models.user import User
from .. import bp


@bp.route("/users", methods=["GET"])
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', [10])
def users():
    q_users = User.read(all_rows=True, order_by="created")

    return render_template(
        bp.tmpl("users.html"),
        q_users=q_users
    )
