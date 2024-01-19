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
    id: int = Field(..., example=1)
    name: str = Field(..., example="Jhon")
    mail: str = Field(..., example="toto@gmail.com")
    birth_date: date = Field(..., example="1999-01-01")
    
class UserInput(BaseModel):
    name: str 
    mail: str
    password: str
    birth_date: date