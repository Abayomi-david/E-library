from typing import List, Optional
from fastapi import HTTPException
from uuid import uuid4
from schemas.users import User, UserCreate, UserUpdate

# Mock in-memory database

users: List[User] = [
    User(id="1", name="Alice Green", email="alice.green@example.com", is_active=True),
    User(id="2", name="Bob Brown", email="bob.brown@example.com", is_active=True),
    User(id="3", name="Charlie Black", email="charlie.black@example.com", is_active=True),
    User(id="4", name="Diana White", email="diana.white@example.com", is_active=True),
    User(id="5", name="Eve Silver", email="eve.silver@example.com", is_active=True),
]
class UserCrud:
    @staticmethod
    def get_user(user_id: str) -> Optional[User]:
        user = next((user for user in users if user.id == user_id), None)
        return user

    @staticmethod
    def get_users() -> List[User]:
        return users

    @staticmethod
    def create_user(user: UserCreate) -> User:
        user_id = str(uuid4())  # Generate a unique UUID for the new user
        new_user = User(id=user_id, **user.model_dump())
        users.append(new_user)
        return new_user

    @staticmethod
    def update_user(user_id: str, data: UserUpdate) -> User:
        user = UserCrud.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.name = data.name
        user.email = data.email
        return user

    @staticmethod
    def delete_user(user_id: str) -> dict:
        user = UserCrud.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        users.remove(user)
        return {"message": "User deleted successfully"}
