from .models import Database

class Violation(Database):
    def __init__(self):
        self.connection = None

    def search_contravenants(self, query):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        search_terms = query.split()
        sql_query = "SELECT * FROM violations WHERE "
        params = []
        for i, term in enumerate(search_terms):
            if i > 0:
                sql_query += " OR "
            sql_query += "etablissement LIKE ? OR proprietaire LIKE ? OR adresse LIKE ?"
            pattern = f"%{term}%"
            params.extend([pattern, pattern, pattern])
        cursor.execute(sql_query, params)
        contravenants = cursor.fetchall()
        connection.close()
        return contravenants
    
    def search_contraventions(self, du, au):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        query = "SELECT * FROM violations where strftime('%s', date) BETWEEN strftime('%s', ?) AND strftime('%s', ?)"
        cursor.execute(query, (du, au))
        contraventions = cursor.fetchall()
        connection.close()
        return contraventions
    
    