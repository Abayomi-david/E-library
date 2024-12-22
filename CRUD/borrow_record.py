from fastapi import HTTPException
from datetime import datetime
from uuid import uuid4
from CRUD.users import users

class BorrowCrud:
    borrow_records = [
    {
        "id": "201",
        "user_id": "1",
        "book_id": "101",
        "borrow_date": "2024-12-15",
        "return_date": "2024-12-16",
    },
    {
        "id": "202",
        "user_id": "2",
        "book_id": "102",
        "borrow_date": "2024-12-16",
        "return_date": "2024-12-20",
    },
    {
        "id": "203",
        "user_id": "3",
        "book_id": "103",
        "borrow_date": "2024-12-17",
        "return_date": "2024-12-18",
    },
]

    books = []  
    users = []  

    @staticmethod
    def borrow_book(book_id: str, user_id: str):
        # Check if the user exists and is active
        user = next((u for u in BorrowCrud.users if u["id"] == user_id and u["is_active"]), None)
        if not user:
            raise HTTPException(status_code=404, detail="Active user not found")

        # Check if the book exists and is available
        book = next((b for b in BorrowCrud.books if b["id"] == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        if not book["is_available"]:
            raise HTTPException(status_code=400, detail="Book is not available for borrowing")

        # Check if the user has already borrowed this book
        if any(record["user_id"] == user_id and record["book_id"] == book_id and record["return_date"] is None for record in BorrowCrud.borrow_records):
            raise HTTPException(status_code=400, detail="User has already borrowed this book")

        # Create a borrow record
        borrow_record = {
            "id": str(uuid4()),
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": datetime.now(),
            "return_date": None,
        }
        BorrowCrud.borrow_records.append(borrow_record)

        # Mark the book as unavailable
        book["is_available"] = False

        return {"message": "Book borrowed successfully", "data": borrow_record}
    


    @staticmethod
    def return_book(book_id: str, user_id: str):
        # Find the borrow record for the book and user
        borrow_record = next(
            (record for record in BorrowCrud.borrow_records if record["book_id"] == book_id and record["user_id"] == user_id and record["return_date"] is None),
            None,
        )
        if not borrow_record:
            raise HTTPException(status_code=404, detail="Borrow record not found or book already returned")

        # Find the book and mark it as available
        book = next((b for b in BorrowCrud.books if b["id"] == book_id), None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        book["is_available"] = True

        # Update the borrow record with the return date
        borrow_record["return_date"] = datetime.now()

        return {"message": "Book returned successfully", "data": borrow_record}


    @staticmethod
    def get_all_records():
        return BorrowCrud.borrow_records

    @staticmethod
    def get_user_records(user_id: str):
        return [record for record in BorrowCrud.borrow_records if record["user_id"] == user_id]

    @staticmethod
    def get_book_records(book_id: str):
        return [record for record in BorrowCrud.borrow_records if record["book_id"] == book_id]
