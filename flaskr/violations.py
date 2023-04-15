from .models import Database
from flask import json
class Violation(Database):
    def __init__(self):
        self.connection = None

    def search_contravenants(self, query):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = query.split()
        sql_query = "SELECT * FROM violations WHERE "
        params = []

        for i, mot in enumerate(query):
            if i > 0:
                sql_query += " OR "
            sql_query += "etablissement LIKE ? OR proprietaire LIKE ? OR adresse LIKE ?"
            pattern = f"%{mot}%"
            params.extend([pattern, pattern, pattern])
            
        cursor.execute(sql_query, params)
        contravenants = cursor.fetchall()
        connection.close()
        return contravenants
    
    def search_contraventions(self, du, au):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = "SELECT * FROM violations WHERE date >= ? AND date <= ?"
        cursor.execute(query, (du, au))
        rows = cursor.fetchall()
        connection.close()

        result = []
        for row in rows:
            result.append(dict(row))

        return json.dumps(result)
    
    def search_distinct_etablissement(self):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = "SELECT DISTINCT etablissement FROM violations"
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()

        result = []
        for row in rows:
            result.append(dict(row))

        return json.dumps(result)