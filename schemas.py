from pydantic import BaseModel, HttpUrl
from typing import Optional
import datetime

class UserSchema(BaseModel):
    username: str
    password: str

class TokenSchema(BaseModel):
    refresh: str

class TokenResponseSchema(BaseModel):
    access: str

class UserResponseSchema(BaseModel):
    username: str
    user_type: int
    access: str
    refresh: str
    
class UserInfoSchema(BaseModel):
    username: str
    user_type: int

class UrlSchema(BaseModel):
    origin_url: HttpUrl
    short_string: str
    short_url: HttpUrl
    create_date: datetime.datetime
    expire_date: Optional[datetime.datetime]
    visit_count: int
    creator_username: Optional[str] = None

class ErrorSchema(BaseModel):
    message: str

class UrlCreateSchema(BaseModel):
    origin_url: HttpUrl
    expire_date: Optional[datetime.datetime] = None

class CustomUrlCreateSchema(UrlCreateSchema):
    short_string: str