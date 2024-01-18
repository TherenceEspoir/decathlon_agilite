from http.client import HTTPException
from typing import Union
import uuid

from src.decathlon.connexion import get_connection

from src.decathlon.Model.models import HealthData, Unite

from datetime import datetime

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
                    taille FLOAT,
                    u_taille INTEGER
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
# fonction qui permet de créer un healthData
def create_healthData(healthData: HealthData):
    connection = get_connection()
    connection.execute(
        "INSERT INTO healthData (id, id_user, date, nombre_pas, duree_sommeil, u_duree_sommeil, frequence_cardiaque, u_frequence_cardiaque, poids, u_poids, taille, u_taille) VALUES(?,?,?,?,?,?,?,?,?,?,?,?);",
        (
            str(healthData.uuid) if healthData.uuid else None,
            healthData.id_user,
            healthData.date,
            healthData.nombre_pas,
            healthData.duree_sommeil,
            healthData.u_duree_sommeil,
            healthData.frequence_cardiaque,
            healthData.u_frequence_cardiaque,
            healthData.poids,
            healthData.u_poids,
            healthData.taille,
            healthData.u_taille,
        ),
    )
    connection.commit()
    connection.close()

    return {"Donnée de santé bien ajoutée"}


#fonction qui permet de lister les healthData
def healthData(id_user: int):
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM healthData Where healthData.id_user == ?", (id_user,))
        healthData = cursor.fetchall()

        print(healthData)
        result = []

        for row in healthData:
            try:
                result.append(HealthData(
                    uuid=row[0],
                    id_user=row[1],
                    date=row[2] if row[2] else datetime.now(),
                    nombre_pas=row[3],
                    duree_sommeil=row[4],
                    u_duree_sommeil=row[5],
                    frequence_cardiaque=row[6],
                    u_frequence_cardiaque=row[7],
                    poids=row[8],
                    u_poids=row[9],
                    taille=row[10],
                    u_taille=row[11],
                ))
            except Exception as e:
                print(f"Error processing row {row}: {e}")

    return {"health data: {}".format(result)}


