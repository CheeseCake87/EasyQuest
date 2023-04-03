from flask import render_template

from .. import bp


@bp.route("/quest/<quest_id>", methods=["GET"])
def quest(quest_id):
    quest_id = int(quest_id)

    return render_template(bp.tmpl("quest.html"), quest_id=quest_id)
