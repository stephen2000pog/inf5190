import sqlite3

connection = sqlite3.connect('flaskr/db/violations.db')

with open('flaskr/db/db.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

connection.commit()
connection.close()