from fastapi import Depends, FastAPI, Header, HTTPException

import src.decathlon.Controller.health as health

from src.decathlon.Model.health import HealthData
# from src.decathlon.Model.health import HealthData

from datetime import datetime

import uuid  # Importe le module uuid





app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Hello, Api decathlon en cours de construction"}


# HEALTH DATA


@app.post("/SaisirDonnee", tags=["HEALTH DATA"])
def SaisirDonnee(donnee: HealthData):
    return health.create_healthData(donnee)

@app.get("/getHealthData/{id_user}", tags=["HEALTH DATA"])
def getHealthData(id_user : int):
    return health.healthData(id_user)











health_data_instance_1 = HealthData(
    uuid=uuid.uuid4(),  # Utilise uuid.uuid4() pour générer un uuid aléatoire
    id_user=0,
    date=datetime.now(),
    nombre_pas=1000,
    duree_sommeil=1,
    u_duree_sommeil=1,  # Exemple de valeur pour l'unité de durée de sommeil
    frequence_cardiaque=10,
    u_frequence_cardiaque=1,  # Exemple de valeur pour l'unité de fréquence cardiaque
    poids=10,
    u_poids=1,  # Exemple de valeur pour l'unité de poids
    taille=1,
    u_taille=1  # Exemple de valeur pour l'unité de taille
)



health_data_instance_2 = HealthData(
    uuid=uuid.uuid4(),  # Utilise uuid.uuid4() pour générer un uuid aléatoire
    id_user=1,
    date=datetime.now(),
    nombre_pas=2000,
    duree_sommeil=2,
    u_duree_sommeil=2,  # Exemple de valeur pour l'unité de durée de sommeil
    frequence_cardiaque=20,
    u_frequence_cardiaque=2,  # Exemple de valeur pour l'unité de fréquence cardiaque
    poids=20,
    u_poids=2,  # Exemple de valeur pour l'unité de poids
    taille=2,
    u_taille=2  # Exemple de valeur pour l'unité de taille
)


SaisirDonnee(health_data_instance_1)
SaisirDonnee(health_data_instance_2)

print(health.healthData(0));
print(health.healthData(1));
