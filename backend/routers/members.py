from fastapi import APIRouter, HTTPException,Depends
from auth import get_current_user
from sqlalchemy.orm import session
from database import get_db
from typing import List
from models import User
import schemas
import crud

router = APIRouter()

# Retrieving all the members from the database
@router.get("/member",response_model=List[schemas.MemberResponse])
def get_member(db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_member(db)

# Adding new members into the database
@router.post("/member",response_model=schemas.MemberResponse)
def add_member(member:schemas.MemberCreate,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.add_member(db,member)

# Deleting a member from the database
@router.delete("/member",response_model=schemas.MemberResponse)
def delete_member(member_id:int,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    db_member = crud.delete_member(db,member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return db_member

# Updating member details into the database
@router.put("/member",response_model=schemas.MemberCreate)
def update_member(member:schemas.MemberCreate,member_id:int,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    db_member = crud.update_member(db,member,member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return db_member

# Getting borrowing history of all the members of the library
@router.get("/member/{id}",response_model=List[schemas.MembersHistory])
def member_history(member_id:int,db:session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_member_history(db,member_id)
