from flask import redirect, url_for

from app import db
from .. import bp


@bp.route("/database", methods=["GET"])
def database():
    db.drop_all()
    db.create_all()
    return redirect(url_for("www.index"))
