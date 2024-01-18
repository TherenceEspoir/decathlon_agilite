from http.client import HTTPException
from typing import Union
import uuid

from src.decathlon.connexion import get_connection

from src.decathlon.Model.models import HealthData, Unite

db_connection=get_connection()
cursor = db_connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='healthData';")

healthData_exists = cursor.fetchone() is not None

#si la table n'existe pas on la crée

if not healthData_exists:
    db_connection.execute(
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
                    taille: FLOAT,
                    u_taille: INTEGER
        );"""
    )
    db_connection.commit()
    
cursor = db_connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user';")

user_exists = cursor.fetchone() is not None

#si la table n'existe pas on la crée

if not user_exists:
    db_connection.execute(
        """
            CREATE TABLE user (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    mail TEXT,
                    password TEXT,
                    birth_date DATETIME
        );"""
    )
    db_connection.commit()

cursor = db_connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='unite';")

unite_exists = cursor.fetchone() is not None

#si la table n'existe pas on la crée

if not unite_exists:
    db_connection.execute(
        """
            CREATE TABLE unite (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    abbreviation TEXT
        );"""
    )
    db_connection.commit()
    
cursor = db_connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='unite_convertion';")

unite_convertion_exists = cursor.fetchone() is not None

#si la table n'existe pas on la crée

if not unite_convertion_exists:
    db_connection.execute(
        """
            CREATE TABLE unite_convertion (
                    from_id TEXT,
                    to_id TEXT,
                    rapport FLOAT
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

