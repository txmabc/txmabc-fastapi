import time
from pydantic import BaseModel
from typing import Optional, Union

class LoginReq(BaseModel):
    username: str
    password: str

class AccessToken(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]
    expires_in: Optional[int]
    
class SuccessRes(BaseModel):
    code: int
    data: AccessToken
    time: int=int(time.time())