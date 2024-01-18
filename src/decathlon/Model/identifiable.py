from datetime import datetime
from pydantic import BaseModel
import typing

import uuid

class Identifiable(BaseModel):
    uuid: typing.Union[uuid.UUID, None]