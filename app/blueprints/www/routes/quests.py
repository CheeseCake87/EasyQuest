from flask import render_template

from app.models.genre import Genre
from app.models.quest import Quest
from .. import bp


@bp.route("/quests", methods=["GET"])
def quests():
    q_quests = Quest.read(all_rows=True, order_by="created")
    q_genres = Genre.read(all_rows=True, order_by="created")

    return render_template(
        bp.tmpl("quests.html"),
        q_quests=q_quests,
        q_genres=q_genres,
    )
