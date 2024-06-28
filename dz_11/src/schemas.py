from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field

class UsersBase(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email_address: str = Field(max_length=50)
    phone_number: str = Field(max_length=50)
    date_of_birth: date
    additional_data: str = Field(max_length=150)

class UsersStatusUpdate(BaseModel):
    done: bool

class UsersResponse(UsersBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True