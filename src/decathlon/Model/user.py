from datetime import datetime
from pydantic import BaseModel
import typing

import uuid

from src.decathlon.Model.identifiable import Identifiable
    
class user(Identifiable):
    id: int
    name: str
    mail: str
    password: str
    birth_date: datetime