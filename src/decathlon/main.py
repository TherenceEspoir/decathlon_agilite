from fastapi import Depends, FastAPI, Header, HTTPException

import src.decathlon.Controller.health as health

from src.decathlon.Model.models import HealthData


app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Hello, Api decathlon en cours de construction"}


# HEALTH DATA


@app.post("/SaisirDonnee", tags=["HEALTH DATA"])
def SaisirDonnee(donnee: HealthData):
    return health.create_healthData(donnee)

@app.get("/ListerDonnee", tags=["HEALTH DATA"])
def ListerDonnee():
    return health.ListeDonnee()