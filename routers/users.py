from fastapi import APIRouter, HTTPException
from schemas.users import UserCreate, UserUpdate, User
from CRUD.users import UserCrud, users
from typing import List


user_router = APIRouter()

@user_router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = UserCrud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.get("/users", response_model=List[User])
def get_users():
    return UserCrud.get_users()

@user_router.post("/users", response_model=User)
def create_user(payload: UserCreate):
    return UserCrud.create_user(payload)

@user_router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, payload: UserUpdate):
    return UserCrud.update_user(user_id, payload)

@user_router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: str):
    return UserCrud.delete_user(user_id)
