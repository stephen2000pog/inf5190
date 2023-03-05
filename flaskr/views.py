from flask import Blueprint, render_template, g, request
from .article import Article

views = Blueprint('views', __name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Article()
    return g._database

@views.route('/')
def home():
    articles = get_db().get_articles(5)
    return render_template("home.html", articles = articles)

@views.route('/admin')
def admin_page():
    articles = get_db().get_all_articles()
    return render_template('admin.html', articles=articles)

@views.route('/admin-modifier/<identifiant>')
def admin_modifier(identifiant):
    article = get_db().get_article_by_id(identifiant)
    return render_template('admin-modifier.html', article=article)

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
    elif request.method == 'GET':
        query = request.args.get('query')
    articles = get_db().search_articles(query)
    return render_template("search.html", articles=articles, query=query)

@views.route('/article/<identifiant>')
def show_article(identifiant):
    article = get_db().get_article_by_id(identifiant)
    if article is None:
        return render_template('404.html'), 404
    return render_template('article.html', article=article)

