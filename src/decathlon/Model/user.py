from datetime import datetime
from pydantic import BaseModel
import typing


class User(BaseModel):
    id: int
    name: str
    mail: str
    password: str
    birth_date: datetime

class UserInput(BaseModel):
    name: str
    mail: str
    password: str
    birth_date: datetime