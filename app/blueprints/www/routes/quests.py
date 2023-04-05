from flask import render_template

from .. import bp
from app.models.quest import Quest


@bp.route("/quests", methods=["GET"])
def quests():
    q_quests = Quest

    return render_template(bp.tmpl("quests.html"))
