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
    