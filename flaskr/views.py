from flask import Blueprint, render_template, g, Flask
from .models import Database
import sqlite3

app = Flask(__name__)

views = Blueprint('views', __name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database() 
    return g._database

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@views.route('/')
def index():
    articles = get_db().get_article()
    return render_template("home.html", articles = articles)

#@views.route('/article/<identifiant>')