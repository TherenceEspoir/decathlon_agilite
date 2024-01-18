import os
import sqlite3

class DecathlonDBManager:
    _instance = None

    def __new__(cls, db_filename="decathlon.db"):
        if cls._instance is None:
            cls._instance = super(DecathlonDBManager, cls).__new__(cls)
            cls._instance.db_filename = db_filename
            cls._instance.db_connection = None
        return cls._instance

    def __enter__(self):
        if self.db_connection is None:
            self.db_connection = sqlite3.connect(self.db_filename)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.db_connection is not None:
            self.db_connection.close()
            self.db_connection = None

    def check_and_create_db(self):
        # Vérifier si la base de données existe déjà
        db_exists = os.path.exists(self.db_filename)

        # Si la base de données n'existe pas, créez-la et les tables
        if not db_exists:
            with self:
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

        # Vérifiez à nouveau si la base de données existe après la fermeture
        db_exists = os.path.exists(self.db_filename)

        if db_exists:
            print("La base de données est lue.")
        else:
            print("La base de données a été créée.")

# Utilisation de la classe avec la gestion de contexte
with DecathlonDBManager() as db_manager:
    db_manager.check_and_create_db()


