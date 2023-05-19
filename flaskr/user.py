from hashlib import scrypt
import json

import bcrypt
from .models import Database

class User(Database):
    def __init__(self, id, nom_complet, adresse_courriel, mot_de_passe):
        self.id = id
        self.nom_complet = nom_complet
        self.adresse_courriel = adresse_courriel
        #self.etablissements_surveilles = etablissements_surveilles
        self.mot_de_passe = mot_de_passe
        self.connection = None

    def saveUser(self, user):
        connection = self.get_connection()
        hashed_mdp = bcrypt.hashpw(user.mot_de_passe.encode('utf-8'), bcrypt.gensalt())
        if user.id is None:
            connection.execute("insert into users(nom_complet, adresse_courriel, mot_de_passe) "
                            "values(?, ?, ?, ?)",
                            (user.nom_complet, user.adresse_courriel, hashed_mdp))
            connection.commit()

            cursor = connection.cursor()
            cursor.execute("select last_insert_rowid()")
            result = cursor.fetchall()
            user.id = result[0][0]
        else:
            connection.execute("update users set nom_complet = ?, adresse_courriel = ?,"
                            "mot_de_passe = ? where rowid = ?",
                            (user.nom_complet, user.adresse_courriel, hashed_mdp,
                                user.id))
            connection.commit()
        return user

    def searchUser(self, nom_complet, mot_de_passe):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE nom_complet=?", (nom_complet,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(mot_de_passe.encode('utf-8'), user[2].encode('utf-8')):
            return user
        else:
            return None

    def asDictionary(self):
        return {"id": self.id,
                "nom_complet": self.nom_complet,
                "adresse_courriel": self.adresse_courriel,
                "mot_de_passe" : self.mot_de_passe}
