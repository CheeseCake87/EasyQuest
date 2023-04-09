import json

from flask import render_template, request, redirect, url_for, flash, session
from flask_bigapp.security import login_check, permission_check

from app.models import dater
from app.models.character import Character
from app.models.genre import Genre
from app.models.quest import Quest
from .. import bp


@bp.get("/quest/<quest_id>")
@login_check('authenticated', 'auth.login')
def quest(quest_id):
    q_quest = Quest.read(id_=quest_id)

    if not q_quest:
        flash("Quest not found", "bad")
        return redirect(url_for("www.quests"))

    character = Character.read(
        fields={
            "fk_quest_id": quest_id,
            "fk_user_id": session.get("user_id"),
        }
    )

    return render_template(
        bp.tmpl("quest.html"),
        q_quest=q_quest,
        character=None if not character else character[0]
    )


@bp.get("/quest/<quest_id>/character-manager")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def quest_character_manager(quest_id):
    q_quest = Quest.read(id_=quest_id)

    if not q_quest:
        flash("Quest not found", "bad")
        return redirect(url_for("www.quests"))

    waiting_characters = Character.read(
        fields={
            "fk_quest_id": quest_id,
            "approved": False,
        }
    )

    approved_characters = Character.read(
        fields={
            "fk_quest_id": quest_id,
            "approved": True,
        }
    )

    return render_template(
        bp.tmpl("quest-character-manager.html"),
        q_quest=q_quest,
        waiting_characters=waiting_characters,
        approved_characters=approved_characters,
    )


@bp.get("/edit/quest/<quest_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def edit_quest(quest_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    q_quest = Quest.read(id_=quest_id)

    if not q_quest:
        flash("Quest not found", "bad")
        return redirect(url_for("www.quests"))

    q_genres = Genre.read(all_rows=True, order_by="created")

    return render_template(
        bp.tmpl("edit-quest.html"),
        q_quest=q_quest,
        q_genres=q_genres,
    )


@bp.get("/make-pending/quest/<quest_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def quest_pending(quest_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    Quest.update(id_=quest_id, values={"live": False})
    flash("Quest is now pending", "good")
    if request.args.get("var") == "edit":
        return redirect(url_for("www.edit_quest", quest_id=quest_id))
    return redirect(url_for("www.quest", quest_id=quest_id))


@bp.get("/make-live/quest/<quest_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def quest_live(quest_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    Quest.update(id_=quest_id, values={"live": True})
    flash("Quest is now live", "good")
    if request.args.get("var") == "edit":
        return redirect(url_for("www.edit_quest", quest_id=quest_id))
    return redirect(url_for("www.quest", quest_id=quest_id))


@bp.post("/add/quest")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def add_quest():
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    title = request.form.get("title")
    fk_genre_id = request.form.get("fk_genre_id")

    new_quest = Quest.create(
        {
            "title": title,
            "fk_genre_id": fk_genre_id,
            "live": False,
            "created": dater(),
        }
    )

    return redirect(url_for("www.edit_quest", quest_id=new_quest.quest_id))


@bp.post("/update/quest/<quest_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def update_quest(quest_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    title = request.form.get("title")
    summary = request.form.get("summary")
    arc_cards = request.form.get("arc_cards")
    fk_genre_id = request.form.get("fk_genre_id")

    arc_cards_json = json.loads(arc_cards)

    Quest.update(
        id_=quest_id,
        values={
            "title": title,
            "summary": summary,
            "arc_cards": arc_cards_json,
            "fk_genre_id": fk_genre_id
        }
    )

    flash("Quest updated", "good")
    return redirect(url_for("www.edit_quest", quest_id=quest_id))


@bp.get("/delete/quest/<quest_id>")
@login_check('authenticated', 'auth.login')
@permission_check('permissions', 'www.index', ['admin'])
def delete_quest(quest_id):
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    Quest.delete(fields={"quest_id": quest_id}, return_deleted=True)
    flash(f"Quest deleted", "good")
    return redirect(url_for("www.quests"))
