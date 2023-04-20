## Installer les dépendances
pip install -r requirements.txt

raml2html flaskr/static/doc.raml > flaskr/templates/doc.html
## Initialiser la base de donnée(déjà initialisé par défaut)
python .\flaskr\init_db.py 

## Lancer le programme
python main.py
## Accéder à l'application
Aller à http://127.0.0.1:5000


python -m venv env
.\env\Scripts\activate
pip freeze > requirements.txt

pip install dicttoxml 
pip install flask-json-schema