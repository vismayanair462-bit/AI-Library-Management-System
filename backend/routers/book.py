from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import session
import schemas
import models
from typing import List
from database import get_db
import crud

router = APIRouter()

# Getting all the books in the library
@router.get("/book",response_model=List[schemas.BookResponse])
def get_books(db:session=Depends(get_db)):
    return crud.get_books(db)

# Adding new books into the system
@router.post("/book",response_model=schemas.BookResponse)
def create_book(book:schemas.BookCreate,db:session=Depends(get_db)):
    return crud.add_book(db,book)

# Deleting the book from the system
@router.delete("/book/{book_id}",response_model=schemas.BookResponse)
def delete_book(book_id:int, db:session=Depends(get_db)):
   deleted_book = crud.delete_book(db,book_id)
   if delete_book is None:
       raise HTTPException(status_code=404, detail="Book not found.")
   return deleted_book

# Updating the book details into the system
@router.put("/book/{book_id}",response_model=schemas.BookResponse)
def update_book(book:schemas.BookCreate,book_id:int,db:session=Depends(get_db)):
   updated_book = crud.update_book(db,book,book_id)
   if updated_book is None:
       raise HTTPException(status_code=404, detail="Book not found.")
   return updated_book
