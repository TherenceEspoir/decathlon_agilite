from datetime import date
from pydantic import BaseModel, Field
import typing


class User(BaseModel):
    id: int
    name: str
    mail: str
    password: str
    birth_date: date

class UserResponse(BaseModel):
    id: int
    name: str
    mail: str
    birth_date: date


    
    

class UserInput(BaseModel):
    name: str
    mail: str
    password: str
    birth_date: date