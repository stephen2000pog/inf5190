import sqlite3

connection = sqlite3.connect('articles.db')

with open('flaskr/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO article (id, titre, identifiant, auteur, date_publication, paragraphe) VALUES (?, ?, ?, ?, ?, ?)",
            (1,'Alice au pays des Merveilles', 'alice', 'Alice Shmirtz', '2018-05-29', "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
            )
           
cur.execute("INSERT INTO article (id, titre, identifiant, auteur, date_publication, paragraphe) VALUES (?, ?, ?, ?, ?, ?)",
            (2,'Laura de la jungle', 'laura', 'Georges Washington', '2009-04-30', "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
            )

connection.commit()
connection.close()