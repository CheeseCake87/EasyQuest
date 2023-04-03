from flask import render_template

from .. import bp


@bp.route("/add/quest", methods=["GET"])
def add_quest():

    return render_template(bp.tmpl("add-quest.html"))
