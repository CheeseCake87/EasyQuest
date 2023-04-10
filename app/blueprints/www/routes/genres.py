from flask import render_template, redirect, url_for, session
from flask_bigapp.security import login_check

from app.models.genre import Genre
from .. import bp


@bp.route("/genres", methods=["GET"])
@login_check('authenticated', 'auth.login')
def genres():
    q_genres = Genre.read(all_rows=True, order_by="created")

    return render_template(bp.tmpl("genres.html"), q_genres=q_genres)
