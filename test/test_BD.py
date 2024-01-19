from src.decathlon.Controller.init_bdd import DecathlonDBManager

class TestBD:
    def test_BD(self):
        with DecathlonDBManager() as db_manager:
            db_manager.check_and_create_db()
            connexion = db_manager.db_connection
            assert connexion is not None, "La connexion à la base de données ne doit pas être nulle"

            cursor = connexion.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            assert len(tables) == 4, "Il devrait y avoir 4 tables dans la base de données"

            table_names = [table[0] for table in tables]
            assert 'healthData' in table_names, "La table 'healthData' devrait exister"
            assert 'user' in table_names, "La table 'user' devrait exister"
            assert 'unite' in table_names, "La table 'unite' devrait exister"
            assert 'unite_convertion' in table_names, "La table 'unite_convertion' devrait exister"
