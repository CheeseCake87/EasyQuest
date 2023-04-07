import os

from flask import render_template, redirect, url_for, session, request, flash

from app.extensions import bigapp, security, auth
from app.globals.email import send_email
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


@bp.route("/forgot-password", methods=["GET"])
def forgot_password():
    return redirect(url_for('forgot-password.login'))


@bp.route("/send-new-password", methods=["POST"])
def send_new_password():
    email_address = request.form.get('email_address', None)

    if not email_address:
        flash('Please enter your email address', 'bad')
        return redirect(url_for('forgot-password.login'))

    email_body = f"""
    <p>Hi,</p>
    <p>Here is your new password for EasyQuest:</p>
    <p><strong>{auth.generate_password(style="animals", length=3)}</strong></p>
    <p>Thanks,</p>
    <p>EasyQuest</p>
    """

    send_email(
        os.environ.get("EMAIL_ACCOUNT"),
        f"Your New Password for EasyQuest",
        [email_address],
        email_body,
        "EasyQuest",
        os.environ.get("EMAIL_ACCOUNT"),
        os.environ.get("EMAIL_ACCOUNT"),
        os.environ.get("EMAIL_PASSWORD"),
        "smtp-mail.outlook.com",
        587,
    )

    flash('Your new password has been sent to your email address', 'good')
    return redirect(url_for('auth.login'))


@bp.route("/check-your-emails", methods=["GET"])
def check_emails():
    return render_template(bp.tmpl("check-emails.html"))
