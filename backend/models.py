from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    author = Column(String,nullable=False)
    publication_year = Column(Integer,nullable=False)
    genre = Column(String,nullable=False)
    rating = Column(Float,nullable=False)
    language = Column(String,nullable=False)
    available = Column(Boolean,default=True)
