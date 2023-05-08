import json
from .models import Database

class User(Database):
    def __init__(self, id, nom_complet, adresse_courriel, etablissements_surveilles, mot_de_passe):
        self.id = id
        self.nom_complet = nom_complet
        self.adresse_courriel = adresse_courriel
        self.etablissements_surveilles = etablissements_surveilles
        self.mot_de_passe = mot_de_passe
        self.connection = None

    def saveUser(self, user):
        connection = self.get_connection()
        if user.id is None:
            connection.execute("insert into users(nom_complet, adresse_courriel, etablissements_surveilles, mot_de_passe) "
                            "values(?, ?, ?, ?)",
                            (user.nom_complet, user.adresse_courriel, json.dumps(user.etablissements_surveilles), user.mot_de_passe))
            connection.commit()

            cursor = connection.cursor()
            cursor.execute("select last_insert_rowid()")
            result = cursor.fetchall()
            user.id = result[0][0]
        else:
            connection.execute("update users set nom_complet = ?, adresse_courriel = ?,"
                            "etablissements_surveilles = ?, mot_de_passe = ? where rowid = ?",
                            (user.nom_complet, user.adresse_courriel, json.dumps(user.etablissements_surveilles), user.mot_de_passe,
                                user.id))
            connection.commit()
        return user


    def asDictionary(self):
        return {"id": self.id,
                "nom_complet": self.nom_complet,
                "adresse_courriel": self.adresse_courriel,
                "etablissements_surveilles": self.etablissements_surveilles,
                "mot_de_passe" : self.mot_de_passe}
