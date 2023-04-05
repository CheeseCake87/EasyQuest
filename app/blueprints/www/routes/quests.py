from flask import render_template

from app.models.quest import Quest
from app.models.genre import Genre
from .. import bp


@bp.route("/quests", methods=["GET"])
def quests():
    q_live_quests = Quest.read(fields={"live": True}, order_by="created")
    q_pending_quests = Quest.read(fields={"live": False}, order_by="created")

    q_genres = Genre.read(all_rows=True, order_by="created")

    return render_template(
        bp.tmpl("quests.html"),
        q_live_quests=q_live_quests,
        q_pending_quests=q_pending_quests,
        q_genres=q_genres,
    )
