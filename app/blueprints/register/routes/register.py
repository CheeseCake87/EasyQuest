import os

from flask import render_template, request, flash, redirect, url_for, session

from app.extensions import auth
from app.globals.email import send_email
from app.models.user import User
from .. import bp


@bp.get("/")
def register():
    return render_template(bp.tmpl("register.html"))


@bp.post("/")
def register_post():
    first_name = request.form.get('first_name', None)
    email_address = request.form.get('email_address', None)
    password = request.form.get('password', None)
    password_confirm = request.form.get('password_confirm', None)
    if password != password_confirm:
        flash('Passwords do not match', 'bad')
        session.get('temp', {}).update({
            'first_name': first_name,
        })
        return redirect(url_for('register.register'))

    if User.exists(email_address=email_address):
        flash('Email address already in use', 'bad')
        session.get('temp', {}).update({
            'first_name': first_name,
        })
        return redirect(url_for('register.register'))

    salt = auth.generate_salt()
    password = auth.sha_password(password, salt)
    passport = auth.generate_numeric_validator(6)

    user = User.create(fields={
        'first_name': first_name,
        'email_address': email_address,
        'password': password,
        'salt': salt,
        'passport': passport,
        'user_type': 1
    })

    session['user_id'] = user.user_id
    session['passport'] = user.passport
    session['authenticated'] = True

    email_body = f"""
        <p>Hello,</p>
        <p>Welcome to EasyQuest. That is all.</p>
        <p>Thanks,</p>
        <p>Bye</p>
        """

    send_email(
        os.environ.get("EMAIL_ACCOUNT"),
        f"Welcome to EasyQuest",
        [email_address],
        email_body,
        "EasyQuest",
        os.environ.get("EMAIL_ACCOUNT"),
        os.environ.get("EMAIL_ACCOUNT"),
        os.environ.get("EMAIL_PASSWORD"),
        "smtp-mail.outlook.com",
        587,
    )

    flash('Registration successful', 'good')
    return redirect(url_for('www.quests'))
