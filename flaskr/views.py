from flask import Blueprint, render_template, g, request, redirect
from .article import Article
import re
from datetime import datetime

views = Blueprint('views', __name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Article()
    return g._database

@views.route('/')
def home():
    articles = get_db().get_articles_of_the_day(5)
    return render_template("home.html", articles = articles)

@views.route('/search')
def search():
    query = request.args.get('query')
    articles = get_db().search_articles(query)
    return render_template("search.html", articles=articles, query=query)

@views.route('/admin')
def admin_page():
    articles = get_db().get_all_articles()
    return render_template('admin.html', articles=articles)

@views.route('/article/<identifiant>')
def show_article(identifiant):
    article = get_db().get_article_by_id(identifiant)
    if article is None:
        return render_template('404.html'), 404
    return render_template('article.html', article=article)

@views.route('/admin-modifier/<identifiant>')
def admin_modifier(identifiant):
    article = get_db().get_article_by_id(identifiant)
    return render_template('admin-modifier.html', article=article)

@views.route('/admin-post', methods=['POST'])
def admin_post():
    identifiant = request.form['identifiant']
    titre = request.form['titre']
    paragraphe = request.form['paragraphe']
    get_db().update_article(identifiant, titre, paragraphe)
    return redirect('/admin')

@views.route('/admin-nouveau')
def admin_nouveau():
    return render_template('admin-nouveau.html')

@views.route('/creation-article', methods=['POST'])
def create_article():
    titre_valid = True
    identifiant_valid = True
    auteur_valid = True
    date_valid = True
    paragraphe_valid = True

    if request.method == 'POST':
        titre = request.form['titre']
        identifiant = request.form['identifiant']
        auteur = request.form['auteur']
        date_publication = request.form['date_publication']
        paragraphe = request.form['paragraphe']

        titre_valid = validate_titre(titre)
        identifiant_valid = validate_identifiant(identifiant)
        auteur_valid = validate_auteur(auteur)
        date_valid = validate_date(date_publication)
        paragraphe_valid = validate_paragraphe(paragraphe)

        if not (titre_valid and identifiant_valid and auteur_valid and date_valid and paragraphe_valid):
            return render_template('admin-nouveau.html', 
                                titre_valid = titre_valid,
                                identifiant_valid = identifiant_valid,
                                auteur_valid = auteur_valid,
                                date_valid = date_valid,
                                paragraphe_valid = paragraphe_valid,
                                titre=titre,
                                identifiant=identifiant,
                                auteur=auteur,
                                date_publication=date_publication,
                                paragraphe=paragraphe)
        else:
            get_db().insert_article(titre, identifiant,
                                    auteur, date_publication, paragraphe)
            return redirect('/admin')

def validate_titre(titre):
    pattern = r'^[a-zA-Z0-9\s]{1,100}$'
    return bool(re.match(pattern, titre))

def validate_identifiant(identifiant):
    pattern = r'^[a-zA-Z0-9\s]{1,50}$'
    return bool(re.match(pattern, identifiant))

def validate_auteur(auteur):
    pattern = r'^[a-zA-Z0-9\s]{1,100}$'
    return bool(re.match(pattern, auteur))

def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validate_paragraphe(paragraphe):
    if len(paragraphe) > 500 or len(paragraphe) < 1:
        return False
    return True

 


