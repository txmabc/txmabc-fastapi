from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List, Any


class CreateInstitution(BaseModel):
    title: Optional[str]
    name: Optional[str]
    mobile: Optional[str]