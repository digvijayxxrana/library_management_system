from fastapi import FastAPI,Depends,HTTPException
from dependency.depens import get_service
from schemas.schemas import StudentCreate,BookCreate,UpdateStudentRequest,BorrowBook,DeleteStudentRequest,StudentResponse,BorrowResponse
from services.services import LibraryService
from typing import List

app = FastAPI()

@app.get("/students",response_model=List[StudentResponse])
def list_students(service:LibraryService = Depends(get_service)):
    return service.list_students()

@app.post("/students",response_model=StudentResponse)
def add_student(payload:StudentCreate,service:LibraryService = Depends(get_service)):
    return service.add_student(payload)

@app.put("/students")
def update_student(payload:UpdateStudentRequest,service:LibraryService = Depends(get_service)):
    return service.update_student(payload)


@app.delete("/students")
def delete_student(payload:DeleteStudentRequest,service:LibraryService = Depends(get_service)):
    return service.delete_student(payload)

@app.post("/borrow",response_model=BorrowResponse)
def borrow_book(payload:BorrowBook,service:LibraryService = Depends(get_service)):
    return service.borrow_book(payload)