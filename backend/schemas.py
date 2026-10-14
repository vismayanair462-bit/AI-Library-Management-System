from pydantic import BaseModel

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
    phone:int

class MemberResponse(MemberCreate):
    id:int
    class Config:
        from_attribute = True