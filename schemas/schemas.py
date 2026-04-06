from pydantic import BaseModel,Field
from typing import List
from datetime import date


class StudentCreate(BaseModel):
    name: str = Field(min_length=2,max_length=100)
    age: int = Field(gt=0)

class BookCreate(BaseModel):
    title: str = Field(min_length=2,max_length=500)
    author: str = Field(min_length=2,max_length=100)
    quantity: int = Field(ge=1)

class UpdateStudentRequest(BaseModel):
    id: int = Field(gt=0)
    new_name: str = Field(min_length=2,max_length=100)
    age: int = Field(gt=0)


class BookItemRequest(BaseModel):
    book_id: int = Field(gt=0)
    days: int = Field(gt=0)

class BorrowBook(BaseModel):
    student_id: int = Field(gt=0)
    books:List[BookItemRequest]

class DeleteStudentRequest(BaseModel):
    id: int = Field(gt=0)
    
class StudentResponse(BaseModel):
    id: int
    name: str

class BookResponse(BaseModel):
    id: int
    title: str
    quantity: int

class BookItemResponse(BaseModel):
    book_id: int
    book_title: str
    days: int
    return_date: date
    status: str

class BorrowResponse(BaseModel):
    student_id: int
    student_name: str
    books: List[BookItemResponse]