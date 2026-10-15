from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime
from sqlalchemy.sql import func
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

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    phone = Column(String,nullable=False)

class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    bio = Column(Text,nullable=True)
    created_at = Column( DateTime(timezone=True),server_default=func.now(),nullable=False)
