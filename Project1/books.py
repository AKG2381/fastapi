from fastapi import Body,FastAPI

app = FastAPI()

BOOKS =  [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    {"title": "1984", "author": "George Orwell", "category": "Science Fiction"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classic"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Romance"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Literary Fiction"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"}
]

@app.get('/books')
async def read_all_books():
    return BOOKS

# @app.get('/books/mybook')
# async def read_all_books():
#     return {'book_title' : "My Favorite Book"}


# path parameters
@app.get('/books/{book_title}')
async def read_all_books(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
# querry paramters
@app.get('/books/')
async def  read_category_by_query(category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append( book)
    return books_to_return


# path and querry parameter
@app.get('/books/{book_author}')
async def read_author_by_category_query(book_author : str,category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append( book)
    return books_to_return

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def updaate_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
    

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title : str):
     for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get('/books/byauthor/{book_author}')
async def read_author_by_category_query(book_author : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() :
            books_to_return.append( book)
    return books_to_return