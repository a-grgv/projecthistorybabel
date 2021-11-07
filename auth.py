from datetime import datetime, timezone, timedelta

from flask import Blueprint, request, jsonify, render_template, make_response, url_for, flash
from flask_jwt_extended import create_access_token, unset_jwt_cookies, create_refresh_token, set_access_cookies, \
    set_refresh_cookies, get_jwt_identity, get_jwt
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from forms import LoginForm, RegistrationForm
from models.users import User
from services import user_service

auth = Blueprint('auth', __name__, template_folder='templates/auth')


@auth.route('/register', methods=('POST','GET'))
def register():
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
            return render_template('register.html',  form=form, error=error)
    return render_template('register.html', form=form)


@auth.route('/login', methods=('POST', 'GET'))
def login():
    if current_user.is_authenticated:
        return render_template('index.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return render_template('index.html', is_index=True)
    return render_template('login.html', title='Sign In', form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('index.html')
