from .models import Database

class Article(Database):
    def __init__(self):
        self.connection = None

    def get_articles_of_the_day(self, number):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT * FROM article "
        "WHERE date(date_publication) = date('now') "
        "ORDER BY date_publication DESC")
        articles = cursor.fetchmany(number)
        return articles
    
    def get_article_by_id(self, identifiant):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT * FROM article "
        "WHERE identifiant = ?", (identifiant,))
        article = cursor.fetchone()
        return article
    
    def get_all_articles(self):
        cursor = self.get_connection_row().cursor()
        cursor.execute("SELECT titre, identifiant, date_publication "
                       "FROM article")
        articles = cursor.fetchall()
        return articles

    def insert_article(self, titre, identifiant, auteur, date, paragraphe):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        cursor.execute(("INSERT into article(titre, identifiant, auteur, date_publication, paragraphe) "
                        "values(?, ?, ?, ?, ?)"), (titre, identifiant, auteur, date, paragraphe))
        connection.commit()

    def search_articles(self, query):
        connection = self.get_connection_row()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM article "
                       "WHERE titre LIKE ? OR paragraphe LIKE ?", ('%'+query+'%', '%'+query+'%'))
        articles = cursor.fetchall()
        return articles
    
    def update_article(self, identifiant, titre, paragraphe):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE article SET titre=?, paragraphe=? "
                       "WHERE identifiant=?", (titre, paragraphe, identifiant))
        connection.commit()
    