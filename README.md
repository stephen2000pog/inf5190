## Installer les dépendances
pip install -r requirements.txt
## Initialiser la base de donnée(déjà initialisé par défaut)
python .\flaskr\init_db.py 

## Insérer les données dans la base de donnée
python .\flaskr\insert_data.py
## Lancer le programme
python main.py
## Accéder à l'application
Aller à http://127.0.0.1:5000