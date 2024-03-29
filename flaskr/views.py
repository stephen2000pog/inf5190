from flask import Flask, Blueprint, flash, redirect, render_template, g, request, jsonify, make_response, session, url_for
from flask_login import login_required
from .violations import Violation
from .plainte import Plainte
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from flask_json_schema import JsonSchema, JsonValidationError
from .schemas import create_user_schema
from .user import User

views = Blueprint('views', __name__)
app = Flask(__name__)
schema = JsonSchema(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Violation()
    return g._database

def get_db_user():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = User(None, None, None, None, None)
    return g._database

def get_db_plainte():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Plainte()
    return g._database

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/inscription')
def inscription():
    return render_template("inscription.html")

@views.route('/connexion')
def connexion():
    return render_template("connexion.html")

@views.route('/profil')
@login_required  # Decorator to require authentication for accessing the route
def profil():
    

    return render_template('profil.html', plaintes=plaintes)

@views.route('/plainte')
def plainte():
    return render_template("plainte.html")

@views.route('/search')
def search():
    return render_template("search.html")

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

@views.route('/all-contrevenants')
def get_all_contraventions():
    contraventions = get_db().search_distinct_etablissement()
    if not contraventions:
        response = jsonify({"message": "Aucune contravention trouvée pour les dates spécifiées"})
        response.status_code = 404
        return response
    return jsonify(contraventions)

@views.route('/infractions/<etablissement>')
def get_infractions(etablissement):
    infractions = get_db().search_infractions_by_etablissement(etablissement)
    if not infractions:
        response = jsonify({"message": "Aucune infraction trouvée pour l'établissement spécifiée"})
        response.status_code = 404
        return response
    return jsonify(infractions)

@views.route('/etablissements/<format>')
def get_etablissements_ordered_by_most_infractions(format):
    if format == 'json':
        etablissements = get_db().search_etablissements_by_most_infractions('json')
        if not etablissements:
            response = jsonify({"message": "Aucun établissement trouvé"})
            response.status_code = 404
            return response
        return jsonify(etablissements)
    elif format == "xml":
        etablissements = get_db().search_etablissements_by_most_infractions('xml')
        if not etablissements:
            response = make_response("<message>Aucun établissement trouvé</message>")
            response.headers.set('Content-Type', 'application/xml')
            return response
        xml = dicttoxml(etablissements, custom_root='etablissements', attr_type=False)
        return parseString(xml).toprettyxml()
    else:
        response = jsonify({"message": "Format non supporté"})
        response.status_code = 400
        return response

@views.route('/inscription', methods=['POST'])
@schema.validate(create_user_schema)
def create_user():
    data = request.get_json()
    user = User(None, data["nom_complet"], data["adresse_courriel"], data["mot_de_passe"])
    user = get_db_user().saveUser(user)
    if user.id is None:
        response = jsonify({"message": "Échec de la création de l'utilisateur"})
        response.status_code = 500
        return response
    return jsonify(user.asDictionary()), 201

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Recherche de l'utilisateur dans la base de données
        user = get_db_user().searchUser(username, password)
        if user:
            # Authentification réussie
            session['user_id'] = user.id
            return redirect('/profil')
        else:
            # Authentification échouée
            return 'Invalid username or password'

    return render_template('login.html')

@views.route('/traitement-plainte', methods=['POST'])
def traitement_plainte():
    # Traitement de la soumission du formulaire de plainte
    etablissement = request.form['establishmentName']
    addresse = request.form['address']
    ville = request.form['city']
    date_visite = request.form['visitDate']
    nom_client = request.form['clientName']
    description = request.form['description']

    # Effectuer les actions nécessaires avec les données de la plainte
    if get_db_plainte().savePlainte(etablissement, addresse, ville, date_visite, nom_client, description):
        return redirect(url_for('views.confirmation_plainte'))
    else:
        flash("Erreur lors de l'enregistrement de la plainte.", 'error')
        return redirect(url_for('views.plainte'))

@views.route('/confirmation-plainte')
def confirmation_plainte():
    return render_template('confirmation-plainte.html')

@views.route('/doc')
def documentation():
    with open('flaskr/templates/doc.html', 'r', encoding="utf-16") as f:
        html = f.read()
    return render_template(html)
