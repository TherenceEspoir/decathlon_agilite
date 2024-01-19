from http.client import HTTPException
from typing import Union
import uuid

from src.decathlon.Controller.init_bdd import DecathlonDBManager

from src.decathlon.Model.health import HealthData, HealthDataInput

from datetime import datetime

from src.decathlon.Controller.init_bdd import conn, cursor
from dateutil import parser
# from src.decathlon.main import app
from datetime import date

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def health_data_by_user_id(user_id: int):
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

def get_health_history_data_by_user_id(user_id: int, start_date: int, end_date: int):
    try:
        try:
            start_date = parser.parse(start_date)
            end_date = parser.parse(end_date)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid date format")

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
    

def post_health_data(health_data: HealthDataInput):
    try:
        cursor.execute("SELECT id FROM health_data WHERE id_user=? AND date=?",
                       (health_data.id_user, date.today()))
        existing_data_id = cursor.fetchone()

        if existing_data_id:
            cursor.execute("UPDATE health_data SET nombre_pas=?, duree_sommeil=?, u_duree_sommeil=?, "
                           "frequence_cardiaque=?, u_frequence_cardiaque=?, poids=?, u_poids=?, "
                           "taille=?, u_taille=? WHERE id=?",
                           (health_data.nombre_pas, health_data.duree_sommeil, health_data.u_duree_sommeil,
                            health_data.frequence_cardiaque, health_data.u_frequence_cardiaque,
                            health_data.poids, health_data.u_poids,
                            health_data.taille, health_data.u_taille,
                            existing_data_id[0]))
        else:
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
    