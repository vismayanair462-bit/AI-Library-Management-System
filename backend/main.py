from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import session
from typing import List
import models
import schemas
from database import engine,SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

books = []
book_id = 1

class Book(BaseModel):
    title:str=Field(min_length=1)
    author:str=Field(min_length=1)
    publication_year:int=Field(ge=1000)
    genre:str=Field(min_length=1)
    rating:float=Field(ge=0,le=5)
    language:str=Field(min_length=1)
    available: bool=False

@app.get("/")
def home():
    return{"message":"The app is running successfully."}

# Getting all the books in the library
@app.get("/book",response_model=List[schemas.BookResponse])
def get_books(db:session=Depends(get_db)):
    return db.query(models.Book).all()

# Adding new books into the system
@app.post("/book",response_model=schemas.BookResponse)
def create_book(book:schemas.BookCreate,db:session=Depends(get_db)):
    new_book = models.Book(
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        genre=book.genre,
        rating=book.rating,
        language=book.language,
        available=book.available
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Deleting the book from the system
@app.delete("/book/{book_id}",response_model=schemas.BookResponse)
def delete_book(book_id:int, db:session=Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id==book_id).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book not found.")
    book_title = db_book.title
    db.delete(db_book)
    db.commit()
    return{"message":f'{book_title} was deleted successfully from the system.'}

# Updating the book details into the system
@app.put("/book/{book_id}",response_model=schemas.BookResponse)
def update_book(book:schemas.BookCreate,book_id:int,db:session=Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id==book_id).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book not found.")
    db_book.title = book.title
    db_book.author = book.author
    db_book.publication_year = book.publication_year
    db_book.genre = book.genre
    db_book.rating = book.rating
    db_book.language = book.language
    db_book.available = book.available
    db.commit()
    db.refresh(db_book)
    return db_book
