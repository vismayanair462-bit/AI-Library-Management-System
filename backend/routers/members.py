from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import session
from database import get_db
from typing import List
import models
import schemas
import crud

router = APIRouter()

# Retrieving all the members from the database
@router.get("/member",response_model=List[schemas.MemberResponse])
def get_member(db:session=Depends(get_db)):
    return crud.get_member(db)

# Adding new members into the database
@router.post("/member",response_model=schemas.MemberResponse)
def add_member(member:schemas.MemberCreate,db:session=Depends(get_db)):
    return crud.add_member(db,member)

# Deleting a member from the database
@router.delete("/member",response_model=schemas.MemberResponse)
def delete_member(member_id:int,db:session=Depends(get_db)):
    db_member = crud.delete_member(db,member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return db_member

# Updating member details into the database
@router.put("/member",response_model=schemas.MemberCreate)
def update_member(member:schemas.MemberCreate,member_id:int,db:session=Depends(get_db)):
    db_member = crud.update_member(db,member,member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return db_member
