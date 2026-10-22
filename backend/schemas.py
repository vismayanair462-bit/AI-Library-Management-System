from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title:str
    author_id:int
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

class BorrowRecordCreate(BaseModel):
    book_id:int
    member_id:int

class BorrowRecordResponse(BorrowRecordCreate):
    id:int
    borrow_date: datetime
    return_date: datetime
    status: str
    class Config:
        from_attribute = True

class ReturnBookCreate(BaseModel):
    borrow_record_id:int

class AvailableBooksResponse(BaseModel):
    title:str
    author_name:str
    class Config:
        from_attributes=True

class BorrowedBookResponse(BaseModel):
    book_title:str
    member_name:str
    borrowed_date:datetime
    status:str
    class Config:
        from_attributes=True

class MembersHistory(BaseModel):
    member_name:str
    book_title:str
    borrow_date:datetime
    return_date:datetime|None
    status:str
    class Config:
        from_attributes=True

class BookHistoryResponse(BaseModel):
    book_name:str
    member_name:str
    borrow_date:datetime
    return_date:datetime|None
    status: str
    class Config:
        from_attributes=True

class DashboardStatsResponse(BaseModel):
    total_books:int
    available_books:int
    borrowed_books:int
    total_members:int
    class Config:
        from_attributes=True

class UserCreate(BaseModel):
    name:str
    phone:str|None = None
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    phone:str|None = None
    email:str
    role:str
    created_at: datetime
    class Config:
        from_attributes=True

class UserLogin(BaseModel):
    email:str
    password:str