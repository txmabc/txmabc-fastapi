from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, List

class CreateUser(BaseModel):
    username: str
    password: str
