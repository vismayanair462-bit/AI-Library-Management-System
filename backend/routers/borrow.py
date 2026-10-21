from fastapi import APIRouter,Depends
from typing import List
from sqlalchemy.orm import session
import crud
import schemas
from database import get_db

router = APIRouter()

@router.post("/borrow")
def borrow_book(borrow:schemas.BorrowRecordCreate,db:session=Depends(get_db)):
    return crud.borrow_book(db,borrow)

@router.post("/return")
def return_book(returns:schemas.ReturnBookCreate,db:session=Depends(get_db)):
    return crud.return_book(db,returns)

@router.post("/borrowed",response_model=List[schemas.BorrowedBookResponse])
def borrowed_book(db:session=Depends(get_db)):
    return crud.get_borrowed_books(db)
