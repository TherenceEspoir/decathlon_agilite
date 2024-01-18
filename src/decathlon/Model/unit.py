from datetime import datetime
from pydantic import BaseModel
import typing

import uuid

from src.decathlon.Model.identifiable import Identifiable

class Unite(Identifiable):
    id: int
    name: str
    abbreviation: str