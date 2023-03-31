from .models import Database

class Violation(Database):
    def __init__(self):
        self.connection = None

    def search_contravenants(self, query):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM violations "
                       "WHERE etablissement LIKE ? OR proprietaire LIKE ? OR adresse LIKE ?", ('%'+query+'%', '%'+query+'%', '%'+query+'%'))
        contravenants = cursor.fetchall()           #AND
        return contravenants