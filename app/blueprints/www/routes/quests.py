from flask import render_template

from .. import bp


@bp.route("/quests", methods=["GET"])
def quests():
    return render_template(bp.tmpl("quests.html"))
