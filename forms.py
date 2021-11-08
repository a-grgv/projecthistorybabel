"""
This module contains forms for templates
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', [Length(min=4, max=25)])
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')


class DocumentForm(FlaskForm):
    title = StringField('Article Title', [Length(min=4, max=25)])
    article = TextAreaField('Article Text', render_kw={"rows": 20, "cols": 70})
    submit = SubmitField('Generate')
