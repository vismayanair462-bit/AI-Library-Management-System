from sqlalchemy.orm import session
import models
import schemas

# Database operation for getting all the books from the system
def get_books(db:session):
    return db.query(models.Book).all()

# Database operation for adding new book into the system
def add_book(db:session,book:schemas.BookCreate):
    new_book = models.Book(
            title=book.title,
            author=book.author,
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
            db_book.author = book.author
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