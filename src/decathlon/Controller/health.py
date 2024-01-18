from http.client import HTTPException
from typing import Union
import uuid

from src.decathlon.connexion import get_connection

from src.decathlon.Model.models import HealthData, Unite

db_connection=get_connection()
cursor = db_connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='healthData';")

table_exists = cursor.fetchone() is not None

#si la table n'existe pas on la crée

if not table_exists:
    db_connection.execute(
        """
            CREATE TABLE healthData (
                    id TEXT PRIMARY KEY,
                    poids INTEGER,
                    frequence_cardiaque INTEGER,
                    duree_sommeil INTEGER,
                    nombre_pas INTEGER
        );"""
    )
    db_connection.commit()

db_connection.close()


#fonction qui permet de créer un healthData
def create_healthData(healthData: HealthData):
    connection=get_connection()
    new_uuid = str(uuid.uuid4())
    connection.execute(
        "INSERT INTO healthData (id,poids,frequence_cardiaque, duree_sommeil,nombre_pas) VALUES(?,?,?,?,?);",
        ( 
            new_uuid,
            healthData.poids,
            healthData.frequence_cardiaque,
            healthData.duree_sommeil,
            healthData.nombre_pas
        ),
    )
    connection.commit()
    connection.close()

    return {"Donnée de santé bien ajouté"}

#fonction qui permet de lister les healthData
def ListeDonnee():
    connection=get_connection()
    cursor = connection.execute("SELECT * FROM healthData")
    healthData = cursor.fetchall()
    # # Transformer les tuples récupérés en objets de type HealthData
    result = []
    for row in healthData:
        result.append(HealthData(
            uuid=row[0],
            poids=row[1],
            frequence_cardiaque=row[2],
            duree_sommeil=row[3],
            nombre_pas=row[4],
        ))
    connection.close()
    return {"datas": result}

