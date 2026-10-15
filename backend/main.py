from fastapi import FastAPI
from sqlalchemy.orm import session
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
from routers.book import router as book_router
from routers.members import router as member_router
from routers.authors import router as author_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_router)
app.include_router(member_router)
app.include_router(author_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

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

