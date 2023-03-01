import sqlite3

connection = sqlite3.connect('articles.db')

with open('flaskr/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO article (id, titre, identifiant, auteur, date_publication, paragraphe) VALUES (?, ?, ?, ?, ?, ?)",
            (1,'First Post', 'Content for the first post', 'Alice Shmirtz', '2018-05-29', 'Il etait une fois Alice')
            )


connection.commit()
connection.close()
