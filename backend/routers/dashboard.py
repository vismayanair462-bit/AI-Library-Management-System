from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
import crud
from database import get_db
import models
import schemas

router = APIRouter(prefix="/dashboard",tags=["Dashboard"])

@router.get("/stats",response_model=schemas.DashboardStatsResponse)
def dashboard_stats(db:session=Depends(get_db)):
    return crud.get_library_statistics(db)