from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    author_id = Column(Integer, ForeignKey("authors.author_id"), nullable=False)
    publication_year = Column(Integer,nullable=False)
    genre = Column(String,nullable=False)
    rating = Column(Float,nullable=False)
    language = Column(String,nullable=False)
    available = Column(Boolean,default=True)

    author = relationship(
        "Author",
        back_populates="books"
    )

    borrow_record = relationship(
        "BorrowRecord",
        back_populates="book"
    )

    

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    phone = Column(String,nullable=False)

    borrow_record = relationship(
            "BorrowRecord",
            back_populates="member"
        )

class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    bio = Column(Text,nullable=True)
    created_at = Column( DateTime(timezone=True),server_default=func.now(),nullable=False)

    books = relationship(
        "Book",
        back_populates="author"
    )

class BorrowRecord(Base):
    __tablename__ = "borrowRecords"
    id = Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("books.id"),nullable=False)
    member_id = Column(Integer,ForeignKey("members.id"),nullable=False)
    borrow_date = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    return_date = Column(DateTime(timezone=True),nullable=True)
    status = Column(String,default="Borrowed")

    book = relationship("Book",back_populates="borrow_record")
    member = relationship("Member",back_populates="borrow_record")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    phone = Column(String)
    email = Column(String, unique=True,nullable=False)
    role = Column(String,nullable=False,default="member")
    hashed_password = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)