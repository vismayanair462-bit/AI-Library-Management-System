from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

books = []
book_id = 1

class Book(BaseModel):
    title:str=Field(min_length=1)
    author:str=Field(min_length=1)
    publication_year:int=Field(ge=1000)
    genre:str=Field(min_length=1)
    rating:int=Field(ge=0,le=5)
    language:str=Field(min_length=1)
    available: bool=False

@app.get("/")
def home():
    return{"message":"The app is running successfully."}

# Getting all the books in the library
@app.get("/book")
def get_book():
    return books

# Adding new books into the system
@app.post("/book")
def add_book(book:Book):
    global book_id
    new_book={
        "id":book_id,
        "title":book.title,
        "author":book.author,
        "publication_year":book.publication_year,
        "genre": book.genre,
        "rating": book.rating,
        "language": book.language,
        "available": book.available
    }
    books.append(new_book)
    book_id+=1
    return{"message":f"{book.title} was successfully added into the system."}

# Deleting the book from the system
@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return{"message":f'{book['title']} was removed from the system.'}
    raise HTTPException(status_code=404, detail="Book not found.")

# Updating the book details into the system
@app.put("/book/{book_id}")
def update_book(book_data:Book,book_id:int):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["publication_year"] = book_data.publication_year
            book["genre"] = book_data.genre
            book["rating"] = book_data.rating
            book["language"] = book_data.language
            book["available"] = book_data.available
            return{"message":"The book details has been updated."}
    raise HTTPException(status_code=404,detail="Book not found.")

