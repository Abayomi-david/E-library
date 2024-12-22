from fastapi import APIRouter, HTTPException
from CRUD.borrow_record import BorrowCrud

borrow_router = APIRouter()

@borrow_router.post("/borrow/{book_id}/{user_id}")
def borrow_book(book_id: str, user_id: str):
    return BorrowCrud.borrow_book(book_id, user_id)


@borrow_router.post("/return/{book_id}/{user_id}")
def return_book(book_id: str, user_id: str):
    return BorrowCrud.return_book(book_id, user_id)


@borrow_router.get("/records")
def get_all_borrow_records():
   
    if not BorrowCrud.borrow_records:
        return {"message": "No borrow records available", "data": []}
    return {"message": "success", "data": BorrowCrud.borrow_records}


@borrow_router.get("/records/book/{book_id}")
def get_book_borrow_records(book_id: str):
    
    book_records = BorrowCrud.get_book_records(book_id)
    if not book_records:
        raise HTTPException(status_code=404, detail="No borrow records found for this book")
    return {"message": "success", "data": book_records}


@borrow_router.get("/records/user/{user_id}")
def get_user_borrow_records(user_id: str):
    
    user_records = BorrowCrud.get_user_records(user_id)
    if not user_records:
        raise HTTPException(status_code=404, detail="No borrow records found for this user")
    return {"message": "success", "data": user_records}


@borrow_router.get("/records")
def get_all_borrow_records():
    
    records = BorrowCrud.get_all_records()
    if not records:
        return {"message": "No borrow records available", "data": []}
    return {"message": "success", "data": records}
