from flask import Blueprint, render_template, g, request, redirect
from .violations import Violation
from datetime import datetime

views = Blueprint('views', __name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Violation()
    return g._database

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/search-result')
def search_result():
    query = request.args.get('query')
    contravenants = get_db().search_contravenants(query)
    return render_template("search-result.html", contravenants=contravenants, query=query)