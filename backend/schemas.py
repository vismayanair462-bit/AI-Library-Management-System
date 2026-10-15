from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title:str
    author:str
    publication_year: int
    genre:str
    rating:float
    language:str
    available:bool

class BookResponse(BookCreate):
    id:int
    class Config:
        from_attributes = True

class MemberCreate(BaseModel):
    name:str
    email:str
    phone:str

class MemberResponse(MemberCreate):
    id:int
    class Config:
        from_attribute = True

class AuthorCreate(BaseModel):
    name:str
    bio:str|None=None

class AuthorResponse(AuthorCreate):
    author_id:int
    created_at: datetime
    class Config:
        from_attribute = True