from fastapi import APIRouter,Depends
from auth import get_current_user
from sqlalchemy.orm import session
import crud
from database import get_db
from models import User
import schemas

router = APIRouter(prefix="/dashboard",tags=["Dashboard"])

@router.get("/stats",response_model=schemas.DashboardStatsResponse)
def dashboard_stats(db:session=Depends(get_db),current_user: User=Depends(get_current_user)):
    return crud.get_library_statistics(db)