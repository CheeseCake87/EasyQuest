from flask import redirect, url_for
from flask_bigapp.security import login_check, permission_check

from app import db
from .. import bp


@bp.route("/database", methods=["GET"])
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def database():
    db.drop_all()
    db.create_all()
    return redirect(url_for("www.index"))
