from fastapi import Depends, FastAPI, Header, HTTPException
from decathlon.Model.models import HealthData
import decathlon.Controller.health as health


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