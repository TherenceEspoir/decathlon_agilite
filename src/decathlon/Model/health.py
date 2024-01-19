from datetime import date
from pydantic import BaseModel
import typing


class HealthData(BaseModel):
    id_user: int
    date: date
    nombre_pas: int
    duree_sommeil: int
    u_duree_sommeil: int
    frequence_cardiaque: int
    u_frequence_cardiaque: int
    poids: int
    u_poids: int
    taille: float
    u_taille: int
    
        
class HealthDataInput(BaseModel):
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