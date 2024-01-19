from datetime import date
from pydantic import BaseModel, Field
import typing


class User(BaseModel):
    id: int
    name: str = Field(..., example="John")
    mail: str = Field(..., example="toto@gmail.com")
    password: str = Field(..., example="xxxxxx")
    birth_date: date = Field(..., example="1999-01-01")

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