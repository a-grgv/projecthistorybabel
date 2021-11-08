"""
This module defines endpoints for home
"""
from flask import Blueprint, render_template

homes = Blueprint('homes', __name__)


@homes.route('/', methods=['GET'])
def home():
    """
    Home page
    :return:
    """
    return render_template("index.html", is_index=True)
