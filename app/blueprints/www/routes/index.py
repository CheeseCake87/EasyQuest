from flask import url_for, redirect

from app.extensions import security
from .. import bp


@bp.route("/", methods=["GET"])
@security.login_required("auth.login", "authenticated")
def index():
    return redirect(url_for("www.quests"))
