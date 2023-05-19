from .models import Database
from flask import json
class Violation(Database):
    def __init__(self):
        self.connection = None

    def search_contravenants(self, query):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = query.split()
        params = []

        if query:
            sql_query = "SELECT * FROM violations WHERE "
            for i, mot in enumerate(query):
                if i > 0:
                    sql_query += " OR "
                sql_query += "etablissement LIKE ? OR proprietaire LIKE ? OR adresse LIKE ?"
                pattern = f"%{mot}%"
                params.extend([pattern, pattern, pattern])
            
            cursor.execute(sql_query, params)
            contravenants = cursor.fetchall()
        else:
            contravenants = []
        
        return contravenants
 
    def search_contraventions(self, du, au):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = "SELECT * FROM violations WHERE date >= ? AND date <= ?"
        cursor.execute(query, (du, au))
        rows = cursor.fetchall()

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

        result = []
        for row in rows:
            result.append(dict(row))

        return json.dumps(result)
    
    def search_infractions_by_etablissement(self, etablissement):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = "SELECT * FROM violations WHERE etablissement = ?"
        cursor.execute(query, (etablissement,))
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append(dict(row))

        return json.dumps(result)
    
    def search_etablissements_by_most_infractions(self, format):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = """SELECT etablissement, COUNT(*) AS nombre_infractions
                FROM violations
                GROUP BY etablissement
                HAVING nombre_infractions >= 1
                ORDER BY nombre_infractions DESC;"""
        cursor.execute(query)
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append(dict(row))

        if format == 'json':
            return json.dumps(result)
        elif format == 'xml':
            xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
            for infraction in result:
                xml += f'  <etablissement>{infraction["etablissement"]}</etablissement> <infractions>{infraction["nombre_infractions"]}</infractions>"\n'
            return xml
        else:
            raise ValueError(f'Format non valide: {format}')