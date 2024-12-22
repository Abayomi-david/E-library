from uuid import uuid4
from fastapi import HTTPException
from schemas.books import Book, BookCreate, BookUpdate
from datetime import datetime

class BookCrud:
    books = [
    {
        "id": "101",
        "title": "Introduction to Python",
        "author": "James Clear",
        "is_available": True,
    },
    {
        "id": "102",
        "title": "Data Science with R",
        "author": "John Doe",
        "is_available": True,
    },
    {
        "id": "103",
        "title": "Machine Learning Basics",
        "author": "Jane Smith",
        "is_available": True,
    },
    {
        "id": "104",
        "title": "Deep Learning for Beginners",
        "author": "Alice Walker",
        "is_available": True,
    },
    {
        "id": "105",
        "title": "Web Development with Django",
        "author": "Chris Lee",
        "is_available": True,
    },
]

    @staticmethod
    def get_books():
        return {"message": "success", "data": BookCrud.books}

    @staticmethod
    def get_book(book_id: str):
        book = next((book for book in BookCrud.books if book["id"] == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": "success", "data": book}

    @staticmethod
    def create_book(payload: BookCreate):
        book = Book(**payload.model_dump(), id=str(uuid4()))
        BookCrud.books.append(book.dict())
        return {"message": "success", "data": book}

    @staticmethod
    def update_book(book_id: str, payload: BookUpdate):
        book = next((book for book in BookCrud.books if book["id"] == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        book.update(payload.model_dump(exclude_unset=True))
        return {"message": "success", "data": book}

    @staticmethod
    def delete_book(book_id: str):
        book = next((book for book in BookCrud.books if book["id"] == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        BookCrud.books = [b for b in BookCrud.books if b["id"] != book_id]
        return {"message": "success", "data": f"Book with id {book_id} deleted"}

    @staticmethod
    def mark_book_unavailable(book_id: str):
        book = next((book for book in BookCrud.books if book["id"] == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        book["is_available"] = False
        return {"message": "success", "data": book}


