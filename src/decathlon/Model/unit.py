from datetime import datetime
from pydantic import BaseModel
import typing



class Unite(BaseModel):
    id: int
    name: str
    abbreviation: str