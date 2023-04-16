import csv
import sqlite3
import urllib.request

def insert_data():
    url = "https://data.montreal.ca/dataset/05a9e718-6810-4e73-8bb9-5955efeb91a0/resource/7f939a08-be8a-45e1-b208-d8744dca8fc6/download/violations.csv"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    filename = "flaskr/violations.csv"
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read() 

    with open(filename, 'wb') as f:
        f.write(data)

    connection = sqlite3.connect("flaskr/db/violations.db")
    cursor = connection.cursor()

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            # Check if the row already exists in the database
            cursor.execute("""
                SELECT COUNT(*) FROM violations
                WHERE id_poursuite = ? AND business_id = ? AND date = ? AND description = ? AND adresse = ? AND date_jugement = ?
                AND etablissement = ? AND montant = ? AND proprietaire = ? AND ville = ? AND statut = ? AND date_statut = ? AND categorie = ?
            """, row)
            count = cursor.fetchone()[0]
            if count == 0:
                # If the row does not exist, insert it into the database
                cursor.execute("""
                    INSERT INTO violations (id_poursuite, business_id, date, description, adresse, date_jugement, etablissement, montant, proprietaire, ville, statut, date_statut, categorie)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, row)

    connection.commit()
    connection.close()

insert_data()