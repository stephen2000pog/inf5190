import sqlite3
from flask import current_app, g

class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect("flaskr/db/violations.db")
        return self.connection
   
    def get_connection_row(self):
        if self.connection is None:
            self.connection = sqlite3.connect("flaskr/db/violations.db")
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    