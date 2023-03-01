from flask import Blueprint, render_template, g, Flask
from .models import Database
import sqlite3

views = Blueprint('views', __name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database() 
    return g._database


@views.route('/')
def index():
    articles = get_db().get_article()
    return render_template("home.html", articles = articles)

#@views.route('/article/<identifiant>')