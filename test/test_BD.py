import src.decathlon.Controller.init_bdd 
import sqlite3

class TestBD:
    def test_BD(self):
        
        connexion = sqlite3.connect("mydatabase.db")
        assert connexion is not None, "La connexion à la base de données ne doit pas être nulle"

        cursor = connexion.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert len(tables) == 4, "Il devrait y avoir 4 tables dans la base de données"

        table_names = [table[0] for table in tables]
        assert 'health_data' in table_names, "La table 'health_data' devrait exister"
        assert 'users' in table_names, "La table 'users' devrait exister"
        assert 'unites' in table_names, "La table 'unites' devrait exister"
