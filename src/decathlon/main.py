from fastapi import Depends, FastAPI, Header, HTTPException

import src.decathlon.Controller.health as health

from src.decathlon.Model.health import HealthData
# from src.decathlon.Model.health import HealthData
import src.decathlon.Controller.init_bdd

from datetime import datetime

import uuid  # Importe le module uuid





# app = FastAPI()

# @app.get("/")
# def welcome():
#     return {"message": "Hello, Api decathlon en cours de construction"}


# # HEALTH DATA


# @app.post("/SaisirDonnee", tags=["HEALTH DATA"])
# def SaisirDonnee(donnee: HealthData):
#     return health.create_healthData(donnee)

# @app.get("/getHealthData/{id_user}", tags=["HEALTH DATA"])
# def getHealthData(id_user : int):
#     return health.healthData(id_user)











# health_data_instance_1 = HealthData(
#     uuid=uuid.uuid4(),  # Utilise uuid.uuid4() pour générer un uuid aléatoire
#     id_user=0,
#     date=datetime.now(),
#     nombre_pas=1000,
#     duree_sommeil=1,
#     u_duree_sommeil=1,  # Exemple de valeur pour l'unité de durée de sommeil
#     frequence_cardiaque=10,
#     u_frequence_cardiaque=1,  # Exemple de valeur pour l'unité de fréquence cardiaque
#     poids=10,
#     u_poids=1,  # Exemple de valeur pour l'unité de poids
#     taille=1,
#     u_taille=1  # Exemple de valeur pour l'unité de taille
# )



# health_data_instance_2 = HealthData(
#     uuid=uuid.uuid4(),  # Utilise uuid.uuid4() pour générer un uuid aléatoire
#     id_user=1,
#     date=datetime.now(),
#     nombre_pas=2000,
#     duree_sommeil=2,
#     u_duree_sommeil=2,  # Exemple de valeur pour l'unité de durée de sommeil
#     frequence_cardiaque=20,
#     u_frequence_cardiaque=2,  # Exemple de valeur pour l'unité de fréquence cardiaque
#     poids=20,
#     u_poids=2,  # Exemple de valeur pour l'unité de poids
#     taille=2,
#     u_taille=2  # Exemple de valeur pour l'unité de taille
# )


# SaisirDonnee(health_data_instance_1)
# SaisirDonnee(health_data_instance_2)

# print(health.healthData(0))
# print(health.healthData(1))



from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
import sqlite3
from datetime import date
from dateutil import parser

# Connexion à la base de données SQLite
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Création de tables (à ajuster selon vos besoins)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    mail TEXT,
                    password TEXT,
                    birth_date DATETIME)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS unites (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    abbreviation TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS health_data (
                    id INTEGER PRIMARY KEY,
                    id_user INTEGER,
                    date DATETIME,
                    nombre_pas INTEGER,
                    duree_sommeil INTEGER,
                    u_duree_sommeil INTEGER,
                    frequence_cardiaque INTEGER,
                    u_frequence_cardiaque INTEGER,
                    poids INTEGER,
                    u_poids INTEGER,
                    taille REAL,
                    u_taille INTEGER)''')

conn.commit()

# FastAPI application
app = FastAPI()

# Middleware pour permettre les requêtes cross-origin (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vous pouvez ajuster les origines autorisées
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles Pydantic
class Identifiable(BaseModel):
    uuid: Optional[str] = None

class User(Identifiable):
    id: int
    name: str
    mail: str
    password: str
    birth_date: datetime

class Unite(Identifiable):
    id: int
    name: str
    abbreviation: str

class HealthData(Identifiable):
    id: int
    id_user: int
    date: datetime
    nombre_pas: int
    duree_sommeil: int
    u_duree_sommeil: int
    frequence_cardiaque: int
    u_frequence_cardiaque: int
    poids: int
    u_poids: int
    taille: float
    u_taille: int

class HealthDataInput(Identifiable):
    id_user: int
    nombre_pas: int
    duree_sommeil: int
    u_duree_sommeil: int
    frequence_cardiaque: int
    u_frequence_cardiaque: int
    poids: int
    u_poids: int
    taille: float
    u_taille: int

# Routes
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    # Logique pour récupérer un utilisateur par son ID depuis la base de données
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user_data = cursor.fetchone()

    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    user = User(
        id=user_data[0],
        name=user_data[1],
        mail=user_data[2],
        password=user_data[3],
        birth_date=user_data[4]
    )

    return user

@app.post("/users/")
async def create_user(user: User):
    # Logique pour créer un utilisateur dans la base de données
    try:
        cursor.execute("INSERT INTO users (name, mail, password, birth_date) VALUES (?, ?, ?, ?)",
                       (user.name, user.mail, user.password, user.birth_date))
        conn.commit()

        # Récupérer l'ID du dernier utilisateur inséré
        user_id = cursor.lastrowid

        # Mettre à jour l'objet User avec l'ID attribué
        user.id = user_id

        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")

# @app.get("/unites/{unite_id}")
# async def read_unite(unite_id: int):
#     # Logique pour récupérer une unité par son ID depuis la base de données
#     return {"unite_id": unite_id}

# @app.post("/unites/")
# async def create_unite(unite: Unite):
#     # Logique pour créer une unité dans la base de données
#     return unite

@app.get("/health_data/{user_id}")
async def read_health_data(user_id: int):
    # Logique pour récupérer des données de santé par l'ID utilisateur depuis la base de données
    try:
        cursor.execute("SELECT * FROM health_data WHERE id_user=?", (user_id,))
        health_data_list = cursor.fetchall()

        if not health_data_list:
            raise HTTPException(status_code=404, detail="Health data not found for the user")

        health_data_entries = []
        for data in health_data_list:
            health_data = HealthData(
                id=data[0],
                id_user=data[1],
                date=parser.parse(data[2]),
                nombre_pas=data[3],
                duree_sommeil=data[4],
                u_duree_sommeil=data[5],
                frequence_cardiaque=data[6],
                u_frequence_cardiaque=data[7],
                poids=data[8],
                u_poids=data[9],
                taille=data[10],
                u_taille=data[11]
            )
            health_data_entries.append(health_data)

        return health_data_entries
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving health data: {str(e)}")

@app.get("/health_data/{user_id}/{start_date},{end_date}")
async def read_health_data(user_id: int, start_date: str, end_date: str):
    try:
        # Vérifier si les dates fournies sont au format correct
        try:
            start_date = parser.parse(start_date)
            end_date = parser.parse(end_date)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid date format")

        # Logique pour récupérer des données de santé par l'ID utilisateur dans une plage de dates
        cursor.execute("SELECT * FROM health_data WHERE id_user=? AND date BETWEEN ? AND ?",
                       (user_id, start_date, end_date))
        health_data_list = cursor.fetchall()

        if not health_data_list:
            raise HTTPException(status_code=404, detail="Health data not found for the user in the specified date range")

        health_data_entries = []
        for data in health_data_list:
            health_data = HealthData(
                id=data[0],
                id_user=data[1],
                date=parser.parse(data[2]),
                nombre_pas=data[3],
                duree_sommeil=data[4],
                u_duree_sommeil=data[5],
                frequence_cardiaque=data[6],
                u_frequence_cardiaque=data[7],
                poids=data[8],
                u_poids=data[9],
                taille=data[10],
                u_taille=data[11]
            )
            health_data_entries.append(health_data)

        return health_data_entries
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving health data: {str(e)}")
    
    
@app.post("/health_data/")# ajouter un champs optionnal pour mettre une date antérieur
async def create_or_update_health_data(health_data: HealthDataInput):
    # Logique pour créer ou mettre à jour des données de santé dans la base de données
    try:
        # Vérifier si des données existent pour l'utilisateur et la date spécifiée
        cursor.execute("SELECT id FROM health_data WHERE id_user=? AND date=?",
                       (health_data.id_user, date.today()))
        existing_data_id = cursor.fetchone()

        if existing_data_id:
            # Si des données existent, effectuer une mise à jour
            cursor.execute("UPDATE health_data SET nombre_pas=?, duree_sommeil=?, u_duree_sommeil=?, "
                           "frequence_cardiaque=?, u_frequence_cardiaque=?, poids=?, u_poids=?, "
                           "taille=?, u_taille=? WHERE id=?",
                           (health_data.nombre_pas, health_data.duree_sommeil, health_data.u_duree_sommeil,
                            health_data.frequence_cardiaque, health_data.u_frequence_cardiaque,
                            health_data.poids, health_data.u_poids,
                            health_data.taille, health_data.u_taille,
                            existing_data_id[0]))
        else:
            # Si aucune donnée n'existe, effectuer une insertion
            cursor.execute("INSERT INTO health_data (id_user, date, nombre_pas, duree_sommeil, u_duree_sommeil, "
                           "frequence_cardiaque, u_frequence_cardiaque, poids, u_poids, taille, u_taille) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (health_data.id_user, date.today(), health_data.nombre_pas,
                            health_data.duree_sommeil, health_data.u_duree_sommeil,
                            health_data.frequence_cardiaque, health_data.u_frequence_cardiaque,
                            health_data.poids, health_data.u_poids,
                            health_data.taille, health_data.u_taille))

        conn.commit()

        return health_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating or updating health data: {str(e)}")
    