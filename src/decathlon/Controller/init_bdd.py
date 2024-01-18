import os
from src.decathlon.Model.health import HealthData
from src.decathlon.connexion import get_connection

class DecathlonDBManager:
    def __init__(self, db_filename="decathlon.db"):
        self.db_filename = db_filename
        self.db_connection = get_connection()

    def check_and_create_db(self):
        # Vérifier si la base de données existe déjà
        db_exists = os.path.exists(self.db_filename)

        # Si la base de données n'existe pas, créez-la et les tables
        if not db_exists:
            self.db_connection.execute(
                """
                CREATE TABLE healthData (
                    id TEXT PRIMARY KEY,
                    id_user INTEGER,
                    date DATETIME, 
                    nombre_pas INTEGER,
                    duree_sommeil INTEGER,
                    u_duree_sommeil INTEGER,
                    frequence_cardiaque INTEGER,
                    u_frequence_cardiaque INTEGER,
                    poids INTEGER,
                    u_poids INTEGER,
                    taille FLOAT,
                    u_taille INTEGER
                );"""
            )
            self.db_connection.execute(
                """
                CREATE TABLE user (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    mail TEXT,
                    password TEXT,
                    birth_date DATETIME
                );"""
            )
            self.db_connection.execute(
                """
                CREATE TABLE unite (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    abbreviation TEXT
                );"""
            )
            self.db_connection.execute(
                """
                CREATE TABLE unite_convertion (
                    from_id TEXT,
                    to_id TEXT,
                    rapport FLOAT
                );"""
            )
            self.db_connection.commit()

        # Fermez la connexion à la base de données
        self.db_connection.close()

        # Vérifiez à nouveau si la base de données existe après la fermeture
        db_exists = os.path.exists(self.db_filename)

        if db_exists:
            print("La base de données est lue.")
        else:
            print("La base de données a été créée.")

# Utilisation de la classe
db_manager = DecathlonDBManager()
db_manager.check_and_create_db()
