from datetime import datetime
from pydantic import BaseModel
import typing

import uuid

class Identifiable(BaseModel):
    uuid: typing.Union[uuid.UUID, None]


class user(Identifiable):
    id: int
    name: str
    mail: str
    password: str
    bearth_date: datetime
    
    
    
#classe unité avec abréviation de l'unité et identifiant
class Unite(Identifiable):
    id: int
    name: str
    abbreviation: str

#Classe healthData avec les différents attributs poids , frequence cardiaque, durée de sommeil, nombre de pas 
    
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
    
    

class Unite_Convertion(Identifiable):
    from_id: int
    to_id: int
    rapport: float


