from flask import render_template

from .. import bp


@bp.route("/", methods=["GET"])
def register():
    return render_template(bp.tmpl("register.html"))

