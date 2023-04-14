from flask import Blueprint, render_template, g, request, redirect, jsonify
from .violations import Violation

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

@views.route('/contrevenants')
def get_contraventions():
    du = request.args.get('du').replace('-', '')
    au = request.args.get('au').replace('-', '')
    contraventions = get_db().search_contraventions(du, au)
    if not contraventions:
        response = jsonify({"message": "Aucune contravention trouvée pour les dates spécifiées"})
        response.status_code = 404
        return response
    return jsonify(contraventions)

@views.route('/doc')
def documentation():
    #with open('flaskr/static/doc.raml', 'r') as f:
    #    documentation = f.read()
    #documentation_html = raml2html.render(documentation)
    return render_template('doc.html')#, documentation_html=documentation_html)