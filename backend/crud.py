from sqlalchemy.orm import session
from datetime import datetime,timezone
from fastapi import HTTPException
import models
import schemas


# Database operation for getting all the books from the system
def get_books(db:session):
    return db.query(models.Book).all()

# Database operation for adding new book into the system
def add_book(db:session,book:schemas.BookCreate):
    new_book = models.Book(
            title=book.title,
            author_id=book.author_id,
            publication_year=book.publication_year,
            genre=book.genre,
            rating=book.rating,
            language=book.language,
            available=book.available
        )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Database operation for deleting a book from the system
def delete_book(db:session,book_id:int):
        db_book = db.query(models.Book).filter(models.Book.id==book_id).first()
        if not db_book:
            return None
        db.delete(db_book)
        db.commit()
        return db_book

# Database operation for updating book details into the system
def update_book(db:session,book:schemas.BookCreate,book_id:int):
            db_book = db.query(models.Book).filter(models.Book.id==book_id).first()
            if not db_book:
                return None
            db_book.title = book.title
            db_book.author_id = book.author_id
            db_book.publication_year = book.publication_year
            db_book.genre = book.genre
            db_book.rating = book.rating
            db_book.language = book.language
            db_book.available = book.available
            db.commit()
            db.refresh(db_book)
            return db_book

# Database operation to retrieve all the member information from the database
def get_member(db:session):
      return db.query(models.Member).all()

# Database operation to add new members into the database
def add_member(db:session,member:schemas.MemberCreate):
      new_member = models.Member(
            name = member.name,
            email = member.email,
            phone = member.phone
      )
      db.add(new_member)
      db.commit()
      db.refresh(new_member)
      return new_member

# Database operations to delete a member from the database
def delete_member(db:session,member_id:int):
      db_member = db.query(models.Member).filter(models.Member.id == member_id).first()
      if not db_member:
            return None
      db.delete(db_member)
      db.commit()
      return db_member

# Database operation to update member details into the database
def update_member(db:session,member:schemas.MemberCreate,member_id:int):
      db_member = db.query(models.Member).filter(models.Member.id == member_id).first()
      if not db_member:
            return None
      db_member.name = member.name
      db_member.email = member.email
      db_member.phone = member.phone
      db.commit()
      db.refresh(db_member)
      return db_member

# Database operations to retrieve all the authors from the database
def get_authors(db:session):
      return db.query(models.Author).all()

# Database operations to add new author into the database
def add_author(db:session,author:schemas.AuthorCreate):
      new_author = models.Author(
            name = author.name,
            bio = author.bio
      )
      db.add(new_author)
      db.commit()
      db.refresh(new_author)
      return new_author

# Database operations to delete an author from the database
def delete_author(db:session,author_id:int):
      db_author = db.query(models.Author).filter(models.Author.author_id == author_id).first()
      if not db_author:
            return None
      db.delete(db_author)
      db.commit()
      return db_author

# Database operations to update author details from the database
def update_author(db:session,author_id:int,author:schemas.AuthorCreate):
      db_author = db.query(models.Author).filter(models.Author.author_id == author_id).first()
      if not db_author:
            return None
      db_author.name = author.name
      db_author.bio = author.bio
      db.commit()
      db.refresh(db_author)
      return db_author

# Database operation to check whether book, member and avialability; update borrow records table
def borrow_book(db:session,borrow:schemas.BorrowRecordCreate):
      # Check if the book exists
      db_borrow = db.query(models.Book).filter(models.Book.id == borrow.book_id).first()
      if not db_borrow:
            raise HTTPException(status_code=400,detail="Book has been borrowed")

      # Check if the member exists
      db_borrow_member = db.query(models.Member).filter(models.Member.id == borrow.member_id).first()
      if not db_borrow_member:
            raise HTTPException(status_code=404, detail="Member not found")

      # Check if the book is available
      if not db_borrow.available:
            raise HTTPException(status_code=400,detail="Book has been borrowed")
      
      # Creating a record for the borrowed book
      db_borrow_book = models.BorrowRecord(
            book_id = borrow.book_id,
            member_id = borrow.member_id
      )

      # Mark borrowed books as unavailable
      db_borrow.available = False

      db.add(db_borrow_book)
      db.commit()
      db.refresh(db_borrow_book)
      return {"message":f"{db_borrow.title} was borrowed by {db_borrow_member.name}"}

# Database operation for returning book and updating the bookRecords table
def return_book(db:session,returns:schemas.ReturnBookCreate):
      # Find the borrowed book
      db_return = db.query(models.BorrowRecord).filter(models.BorrowRecord.id == returns.borrow_record_id).first()

      if not db_return:
            raise HTTPException(status_code=400,detail="Borrow record not found.")

      # Checking the status of the borrowed book
      if db_return.status == 'returned':
            raise HTTPException(status_code=400,detail="Book already returned")

      # Finding the associated book 
      db_return_book = db.query(models.Book).filter(models.Book.id == db_return.book_id).first()

      if not db_return_book:
            raise HTTPException(status_code=404, detail="Book not found.")

      # Update the status of the book to returned
      db_return.status = "returned"
      # Update the date-time of the return in the table
      db_return.return_date = datetime.now(timezone.utc)
      # Set the the book status to available
      db_return_book.available = True

      db.commit()
      db.refresh(db_return)
      return{"message":f"{db_return_book.title} has been returned successfully."}

# Database opration to get all the available books from the books table 
def get_available_books(db:session):
      db_available = db.query(models.Book).filter(models.Book.available==True).all()
      return [
            {
                  "title": book.title,
                  "author_name": book.author.name
            }
            for book in db_available
      ]

# Database operation to get information about the borrowed books
def get_borrowed_books(db:session):
      db_borrowed = db.query(models.BorrowRecord).filter(models.BorrowRecord.status=="Borrowed").all()
      return[
            {
                  "book_title": book.book.title,
                  "member_name": book.member.name,
                  "borrowed_date":book.borrow_date,
                  "status":book.status
            }
            for book in db_borrowed
      ]


# Database operation to get borrowing history of all the patrons of the library
def get_member_history(db:session,member_id:int):
      db_history = db.query(models.BorrowRecord).filter(models.BorrowRecord.member_id==member_id).all()
      return[
            {
            "member_name": book.member.name,
            "book_title": book.book.title,
            "borrow_date": book.borrow_date,
            "return_date": book.return_date,
            "status": book.status
      }
      for book in db_history
      ]

# Database operation to get borrowing history of a book in the library
def get_book_history(db:session,book_id:int):
      db_book_history = db.query(models.BorrowRecord).filter(models.BorrowRecord.book_id==book_id).all()
      return[
            {
                  "book_name": book.book.title,
                  "member_name": book.member.name,
                  "borrow_date": book.borrow_date,
                  "return_date": book.return_date,
                  "status": book.status
            }
            for book in db_book_history
      ]

# Database operation to get importatnt library statistics
def get_library_statistics(db:session):
      # Displaying the total number of books in the system
      total_books = db.query(models.Book).count()

      # Displaying the total number of available books in the system
      available_books = db.query(models.Book).filter(models.Book.available==True).count()

      # Displaying the the total number of borrowed books in the system
      borrowed_books = db.query(models.BorrowRecord).filter(models.BorrowRecord.status=="Borrowed").count()

      # Displaying the total registered members in the library
      total_members = db.query(models.Member).count()

      return{
                  "total_books": total_books,
                  "available_books": available_books,
                  "borrowed_books": borrowed_books,
                  "total_members": total_members
            }
      
