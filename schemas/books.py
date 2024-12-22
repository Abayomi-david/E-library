from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str

class Book(BookBase):
    id: str
    is_available: bool = Field(default_factory=lambda: True)

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str]  
    author: Optional[str]  
    is_available: Optional[bool]  

class BookStatus(BookBase):
    is_available: bool

