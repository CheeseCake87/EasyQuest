from flask import url_for, redirect

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    return redirect(url_for("www.quests"))
