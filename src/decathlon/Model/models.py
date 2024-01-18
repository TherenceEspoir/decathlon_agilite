from datetime import datetime
from pydantic import BaseModel
import typing

import uuid

class Identifiable(BaseModel):
    uuid: typing.Union[uuid.UUID, None]

#classe unité avec abréviation de l'unité et identifiant
class Unite(Identifiable):
    name: str
    abbreviation: str

#Classe healthData avec les différents attributs poids , frequence cardiaque, durée de sommeil, nombre de pas 
    
class HealthData(Identifiable):
    poids: int
    frequence_cardiaque: int
    duree_sommeil: int
    nombre_pas: int