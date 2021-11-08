"""
This module defines blueprint for authorization
"""

from flask import Blueprint, render_template
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash

from forms import LoginForm, RegistrationForm
from models.users import User
from services import user_service

auth = Blueprint('auth', __name__, template_folder='templates/auth')


@auth.route('/register', methods=('POST', 'GET'))
def register():
    """
    User Registration endpoint
    """
    if current_user.is_authenticated:
        return render_template('index.html')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = user_service.get_user_by_username(username=form.username.data)
        if user is None:
            user_service.create_new_user(username=form.username.data, password=form.password.data)
            return render_template('index.html')
        else:
            error = 'Unable to create user. Please try again.'
            return render_template('register.html', form=form, error=error)
    return render_template('register.html', form=form)


@auth.route('/login', methods=('POST', 'GET'))
def login():
    """
    Login endpoint
    :return:
    """
    if current_user.is_authenticated:
        return render_template('index.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            error = 'Invalid username or password'
            return render_template('login.html', error=error, form=form)
        login_user(user, remember=form.remember_me.data)
        return render_template('index.html', is_index=True)
    return render_template('login.html', form=form)


@auth.route("/logout")
@login_required
def logout():
    """
    Logout endpoint
    :return:
    """
    logout_user()
    return render_template('index.html')
