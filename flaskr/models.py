import sqlite3
import click
from flask import current_app, g

class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('articles.db')
        return self.connection
    
    def get_row_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('articles.db')
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_article(self):
        cursor = self.get_row_connection().cursor()
        cursor.execute("SELECT id, titre, identifiant, auteur, date_publication, paragraphe FROM article")
        articles = cursor.fetchall()
        return articles

    def insert_article(self, titre, identifiant, auteur, date, paragraphe):
        connection = self.get_row_connection()
        cursor = connection.cursor()
        cursor.execute(("insert into article(titre, identifiant, auteur, date_publication, paragraphe) "
                        "values(?, ?, ?, ?, ?)"), (titre, identifiant, auteur, date, paragraphe))
        connection.commit()