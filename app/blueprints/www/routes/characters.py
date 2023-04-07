from flask import render_template, session

from app.models.character import Character
from .. import bp


@bp.route("/your-characters", methods=["GET"])
def your_characters():
    q_characters = Character.read(
        field=('fk_user_id', session.get('user_id', 0)), order_by="created"
    )

    return render_template(
        bp.tmpl("your-characters.html"),
        q_characters=q_characters
    )
