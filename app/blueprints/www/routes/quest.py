from flask import render_template, request, redirect, url_for, flash

from app.models.quest import Quest
from app.models.genre import Genre
from .. import bp


@bp.get("/quest/<quest_id>")
def quest(quest_id):
    q_quest = Quest.read(id_=quest_id)

    if not q_quest:
        flash("Quest not found", "bad")
        return redirect(url_for("www.quests"))

    q_genres = Genre.read(all_rows=True, order_by="created")

    return render_template(
        bp.tmpl("quest.html"),
        q_quest=q_quest,
        q_genres=q_genres,
    )


@bp.get("/make-pending/quest/<quest_id>")
def make_pending_quest(quest_id):
    Quest.update(id_=quest_id, fields={"live": False})
    flash("Quest is now pending", "good")
    return redirect(url_for("www.quest", quest_id=quest_id))


@bp.get("/make-live/quest/<quest_id>")
def make_live_quest(quest_id):
    Quest.update(id_=quest_id, fields={"live": True})
    flash("Quest is now live", "good")
    return redirect(url_for("www.quest", quest_id=quest_id))


@bp.post("/add/quest")
def add_quest():
    title = request.form.get("title")
    summary = request.form.get("summary")
    fk_genre_id = request.form.get("fk_genre_id")

    new_quest = Quest.create(
        {
            "title": title,
            "summary": summary,
            "fk_genre_id": fk_genre_id,
            "live": False,
        }
    )

    return redirect(url_for("www.quest", quest_id=new_quest.quest_id))


@bp.post("/update/quest/<quest_id>")
def update_quest(quest_id):
    title = request.form.get("title")
    summary = request.form.get("summary")
    fk_genre_id = request.form.get("fk_genre_id")

    Quest.update(id_=quest_id, values={"title": title, "summary": summary, "fk_genre_id": fk_genre_id})

    flash("Quest updated", "good")
    return redirect(url_for("www.quest", quest_id=quest_id))


@bp.delete("/delete/quest/<quest_id>")
def delete_quest(quest_id):
    deleted_quest = Quest.delete(fields={"quest_id": quest_id}, return_deleted=True)

    flash(f"Deleted quest: {deleted_quest.title}", "good")
    return redirect(url_for("www.quests"))
