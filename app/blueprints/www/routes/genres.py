from flask import render_template, redirect, url_for, session

from app.models.genre import Genre
from .. import bp


@bp.route("/genres", methods=["GET"])
def genres():
    if session.get("user_type") != 10:
        return redirect(url_for("www.index"))

    q_genres = Genre.read(all_rows=True, order_by="created")

    return render_template(bp.tmpl("genres.html"), q_genres=q_genres)
