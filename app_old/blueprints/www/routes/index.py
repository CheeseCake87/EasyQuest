from flask import url_for, redirect
from flask_bigapp.security import login_check

from .. import bp


@bp.route("/", methods=["GET"])
@login_check('authenticated', 'auth.login')
def index():
    return redirect(url_for("www.quests"))
