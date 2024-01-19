from src.decathlon.connexion import get_connection

class TestConnexion:
    def test_connexion(self):
        connexion = get_connection()
        assert connexion != None
        cursor = connexion.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert len(tables) == 4
        table_names = []
        for table in tables:
            table_names.append(table[0])
        assert 'healthData' in table_names
        assert 'user' in table_names
        assert 'unite' in table_names
        assert 'unite_convertion' in table_names