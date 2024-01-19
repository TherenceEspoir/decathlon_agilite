from datetime import datetime
from pydantic import BaseModel, Field
import typing


class User(BaseModel):
    id: int
    name: str
    mail: str
    password: str
    birth_date: datetime

class UserResponse(BaseModel):
    id: int
    name: str
    mail: str
    birth_date: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "mail": "john.doe@example.com",
                "birth_date": "1990-01-01"
            }
        }

    
    

class UserInput(BaseModel):
    name: str
    mail: str
    password: str
    birth_date: datetime