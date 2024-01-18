from http.client import HTTPException
from typing import Union
import uuid

from src.decathlon.connexion import get_connection

from src.decathlon.Model.health import HealthData

from datetime import datetime

db_connection=get_connection()



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


