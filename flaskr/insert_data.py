#lire toutes donnees
#inserer toutes les donnees dans la bd

import csv
import sqlite3
import urllib.request
from urllib.request import Request, urlopen
import logging
#logging.basicConfig(filename='flaskr/logs/app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def insert_data():
    # Téléchargement du fichier CSV
    url = "https://data.montreal.ca/dataset/05a9e718-6810-4e73-8bb9-5955efeb91a0/resource/7f939a08-be8a-45e1-b208-d8744dca8fc6/download/violations.csv"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = Request(url, headers=headers)
    filename = "flaskr/violations.csv"
    urllib.request.urlretrieve(req, filename)
    #urlopen(req).read(filename)
        # Connexion à la base de données SQLite
    connection = sqlite3.connect("flaskr/db/violations.db")
    cursor = connection.cursor()

        # Suppression de toutes les données existantes
        #cursor.execute("DELETE FROM violations")

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

        #logging.info("Mise à jour de la base de donnée")
