from datetime import datetime
from pydantic import BaseModel
import typing

import uuid

from src.decathlon.Model.identifiable import Identifiable



class HealthData(Identifiable):
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