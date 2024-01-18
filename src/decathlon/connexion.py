import sqlite3

#fonction qui connecte à la base de données
def get_connection():
    connexion = sqlite3.connect("decathlon.db")
    return connexion