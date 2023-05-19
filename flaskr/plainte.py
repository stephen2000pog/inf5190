from .models import Database

class Plainte(Database):
    def __init__(self):
        self.connection = None

    def savePlainte(self, etablissement, addresse, ville, date_visite, nom_client, description):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO plaintes (etablissement, addresse, ville, date_visite, nom_client, description) VALUES (?, ?, ?, ?, ?, ?)",
                        (etablissement, addresse, ville, date_visite, nom_client, description))
            connection.commit()
            return True
        except:
            connection.rollback()
            return False

