from fastapi import HTTPException
from schemas.schemas import StudentCreate,BookCreate,BorrowBook,StudentResponse,BookResponse,BorrowResponse,UpdateStudentRequest,DeleteStudentRequest,BookItemResponse
from datetime import datetime,timedelta
from typing import List

class LibraryService:
    def __init__(self,student_repo,book_repo,order_repo):
        self.book_repo = book_repo
        self.student_repo = student_repo
        self.order_repo = order_repo

    
    def add_student(self,payload:StudentCreate):
        student = self.student_repo.add_student(payload.name,payload.age)
        if student is None:
            raise HTTPException(status_code=400,detail="cannot add student")
        return StudentResponse(id=student,
                name=payload.name)
    
    def list_students(self):
        raw_student =  self.student_repo.list_all()
        return[StudentResponse(id=s[0],name=s[1]) for s in raw_student]
    
    def update_student(self,payload:UpdateStudentRequest):
       student_found = self.student_repo.find_student_by_id(payload.id)
       if student_found is None:
           raise HTTPException(status_code=404,detail="cant find student to update")
       updated_student = self.student_repo.update_student(payload.id,payload.new_name,payload.age)
       return {"message":f"{student_found[1]},has been updated"}
    
    def delete_student(self,payload:DeleteStudentRequest):
        student_found = self.student_repo.find_student_by_id(payload.id)
        if student_found is None:
            raise HTTPException(status_code=404,detail="cant find student to delete")
        orders = self.order_repo.find_order_by_student(payload.id)
        for detail in orders:
            self.book_repo.update_book_quantity(detail[2])
        self.order_repo.delete_order(payload.id)
        self.student_repo.delete_student(payload.id)
        return {"message":f"Student {student_found[1]} deleted and stock restored"}
    
    def borrow_book(self,payload:BorrowBook):
        student_found = self.student_repo.find_student_by_id(payload.student_id)
        if student_found is None:
            raise HTTPException(status_code=404,detail="cant find student")
        
        book_details = []
        for book in payload.books:
            book_found = self.book_repo.find_book_by_id(book.book_id)
            if book_found is None:
                raise HTTPException(status_code=404,detail="cant find book")
            if book.days > 14:
                raise HTTPException(status_code=400,detail="enter days less than 14")
            if book_found[3] <= 0:
                raise HTTPException(status_code=400,detail="book not in stock")
            
            return_date = datetime.today().date() + timedelta(days=book.days)
            order_id = self.order_repo.create_order(student_found[0],book.book_id)
            if order_id is None:
                raise HTTPException(status_code=400,detail="cant create order")
            order = self.order_repo.find_order_by_id(order_id)
            
            detail = BookItemResponse(book_id=book_found[0],
                                      book_title=book_found[1],
                                      days= book.days,
                                      return_date=return_date,
                                      status= order[4])
            book_details.append(detail)
            self.book_repo.update_book_quantity(book_found[0],book_found[3] - 1)
        
        response = BorrowResponse(student_id=student_found[0],
                                  student_name=student_found[1],
                              books=book_details)
        return response
        