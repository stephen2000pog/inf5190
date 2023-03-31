#lire toutes donnees
#inserer toutes les donnees dans la bd

import csv
import sqlite3
import urllib.request

# Téléchargement du fichier CSV
url = "https://data.montreal.ca/dataset/05a9e718-6810-4e73-8bb9-5955efeb91a0/resource/7f939a08-be8a-45e1-b208-d8744dca8fc6/download/violations.csv"
filename = "flaskr/violations.csv"
urllib.request.urlretrieve(url, filename)

# Connexion à la base de données SQLite
connection = sqlite3.connect("flaskr/db/violations.db")
cursor = connection.cursor()

# Lecture du fichier CSV et insertion des données dans la base de données
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Ignorer la première ligne d'en-tête
    for row in reader:
        cursor.execute("""
            INSERT INTO violations (id_poursuite, business_id, date, description, adresse, date_jugement, etablissement, montant, proprietaire, ville, statut, date_statut, categorie)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, row)

# Validation des changements et fermeture de la connexion
connection.commit()
connection.close()
