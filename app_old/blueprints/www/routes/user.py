from flask import redirect, url_for, session
from flask_bigapp.security import login_check, permission_check

from app.models.user import User
from .. import bp


@bp.get("/enable/user/<user_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', [10])
def enable_user(user_id):
    User.enable(user_id)
    return redirect(url_for('www.users'))


@bp.get("/disable/user/<user_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', [10])
def disable_user(user_id):
    User.disable(user_id)
    return redirect(url_for('www.users'))
