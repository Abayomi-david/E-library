from fastapi import APIRouter, HTTPException
from uuid import uuid4
from CRUD.books import BookCrud
from schemas.books import (
    Book,
    BookCreate,
    BookUpdate
)

book_router = APIRouter()

books = [
    {
        "title": "The Great Adventure",
        "author": "John Smith",
        "id": "1",
        "is_available": True,
    },
    {
        "title": "Mystery of the Unknown",
        "author": "Jane Doe",
        "id": "2",
        "is_available": True,
    },
    {
        "title": "Python Programming Essentials",
        "author": "David Clark",
        "id": "3",
        "is_available": True,
    },
    {
        "title": "FastAPI in Practice",
        "author": "Emily Johnson",
        "id": "4",
        "is_available": True,
    },
    {
        "title": "Modern Web Development",
        "author": "Chris Lee",
        "id": "5",
        "is_available": True,
    },
]


@book_router.get("/")
def get_books():
    return BookCrud.get_books()


@book_router.get("/{book_id}")
def get_book(book_id: str):
    return BookCrud.get_book(book_id)


@book_router.post("/")
def create_book(payload: BookCreate):
    return BookCrud.create_book(payload)


@book_router.put("/{book_id}")
def update_book(book_id: str, payload: BookUpdate):
    return BookCrud.update_book(book_id, payload)


@book_router.delete("/{book_id}")
def delete_book(book_id: str):
    return BookCrud.delete_book(book_id)


@book_router.patch("/{book_id}/mark-unavailable")
def mark_book_unavailable(book_id: str):
    return BookCrud.mark_book_unavailable(book_id)