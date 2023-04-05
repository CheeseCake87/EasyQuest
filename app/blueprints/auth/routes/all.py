from flask import render_template, redirect, url_for, session, request, flash

from app.extensions import bigapp, security
from app.models.user import User
from .. import bp


@bp.get("/")
def index():
    return redirect(url_for('auth.login'))


@bp.get("/login")
@security.no_login_required('www.quests', 'authenticated')
def login():
    return render_template(bp.tmpl("login.html"))


@bp.post("/login")
def login_post():
    user = User.login(
        email_address=request.form.get('email_address', None),
        password=request.form.get('password', None)
    )
    if user:
        session['user_id'] = user.user_id
        session['user_type'] = user.user_type
        session['passport'] = user.passport
        session['authenticated'] = True
        return redirect(url_for('www.quests'))

    flash('Invalid login credentials', 'bad')
    return redirect(url_for('auth.login'))


@bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    bigapp.init_session()
    return redirect(url_for('auth.login'))
