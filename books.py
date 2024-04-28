from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS



@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


# @app.get('/books/')       
# async def read_category_by_query(category: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == category.casefold():
#             books_to_return.append(book)
#     return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book')
async def delete_book(delete_book: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == delete_book.casefold():
            BOOKS.pop(i)
            
@app.get('/books/')
async def get_author(get_author: str):
    authors = []
    for book in BOOKS:
        if book.get('author').casefold() == get_author.casefold():
            authors.append(book)
    return authors