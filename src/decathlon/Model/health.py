from datetime import date
from pydantic import BaseModel, Field
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
    id_user: int = Field(..., example=1)
    nombre_pas: int = Field(..., example=10000)
    duree_sommeil: int = Field(..., example=8)
    u_duree_sommeil: int = Field(..., example=1)
    frequence_cardiaque: int = Field(..., example=80)
    u_frequence_cardiaque: int = Field(..., example=1)
    poids: int = Field(..., example=80)
    u_poids: int = Field(..., example=1)
    taille: float = Field(..., example=1.80)
    u_taille: int = Field(..., example=1)
