from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    
    
    def __init__(self, id, title, author, description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str
    description: str
    rating: int
    published_year: int

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2016),
    Book(2, 'Fast Api Course', 'codingwithroby', 'A great book!', 5, 2015),
    Book(3, 'Python Pro', 'codingwithroby', 'A good book!', 5, 2012),
    Book(4, 'HP1', 'Author 1', 'A nice book!', 4, 2017),
    Book(5, 'HP2', 'Author 2', 'A very nice book!', 3, 2020),
    Book(6, 'HP3', 'Author 3', 'A very nice book!', 2, 2019),
]

@app.get('/books', status_code=status.HTTP_200_OK)
async def all_books():
    return BOOKS

@app.get('/books/')
async def rating_get(rating: int):
    books_to_get = []
    for book in BOOKS:
        if book.rating == rating:
            books_to_get.append(book)
    return books_to_get

@app.get('/books/get_year')
async def get_year(year: int):
    books_to_get = []
    for book in BOOKS:
        if book.published_year == year:
            books_to_get.append(book)
    return books_to_get

@app.get('/books/{book_id}')
async def book_id_get(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        
@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put('/books/update-book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found') 

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    book_changed = False
    for book in range(len(BOOKS)):
        if BOOKS[book].id == book_id:
            BOOKS.pop(book)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')