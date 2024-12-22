from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
  

class User(UserBase):
    id: str
    is_active: bool = Field(default_factory=lambda: True)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserStatus(UserBase):
    is_active: bool

