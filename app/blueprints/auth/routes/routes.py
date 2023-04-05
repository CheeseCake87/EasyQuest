from flask import render_template, redirect, url_for, session

from app.extensions import bigapp, security
from .. import bp


@bp.get("/")
def index():
    return redirect(url_for('auth.login'))


@bp.get("/login")
@security.no_login_required('www.quests', 'authenticated')
def login():
    print(session)
    return render_template(bp.tmpl("index.html"))


@bp.post("/login")
def login_post():
    session['user_id'] = 1
    session['authenticated'] = True
    return redirect(url_for('www.quests'))


@bp.route("/logout", methods=["GET"])
def logout():
    print(session)
    session.clear()
    bigapp.init_session()
    print(session)
    return redirect(url_for('auth.login'))
