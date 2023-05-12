# Infraction inspections alimentaires ville de Montréal
Le projet consiste à récupérer un ensemble de données provenant de la ville de Montréal et d'offrir des 
services à partir de ces données. Il s'agit de données ouvertes à propos d'établissements ayant reçu des 
constats d'infraction lors d'inspections alimentaires.
## Accéder à l'application en ligne
Aller à https://stephen2000pog.pythonanywhere.com/
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