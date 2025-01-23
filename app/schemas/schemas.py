from pydantic import BaseModel,Field,EmailStr
from typing import Annotated

class UserSchem(BaseModel):
    name:Annotated[str,...,Field(max_length=15,min_length=3)]
    password:Annotated[str,...,Field(max_length=8,min_length=4)]
    email:EmailStr
    