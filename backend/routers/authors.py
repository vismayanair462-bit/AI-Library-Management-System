from fastapi import APIRouter,HTTPException,Depends
from auth import get_current_user
from sqlalchemy.orm import session
from database import get_db
from typing import List
import crud
from models import User
import schemas

router = APIRouter()

# Getting all the authors from the database
@router.get("/author",response_model=List[schemas.AuthorResponse])
def get_author(db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_authors(db)

# Adding new author into the database
@router.post("/author",response_model=schemas.AuthorResponse)
def add_author(author:schemas.AuthorCreate,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.add_author(db,author)

# Deleting an author from the database
@router.delete("/author",response_model=schemas.AuthorResponse)
def delete_author(author_id:int,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    db_author = crud.delete_author(db,author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return db_author

# Updating author details into the database
@router.put("/author",response_model=schemas.AuthorResponse)
def update_author(author:schemas.AuthorCreate,author_id:int,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    db_author = crud.update_author(db,author_id,author)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return db_author

