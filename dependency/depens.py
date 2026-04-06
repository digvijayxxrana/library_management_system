from repositories.repo import StudentRepository
from repositories.book_repo import BookRepository
from repositories.order_repo import OrderRepository
from services.services import LibraryService

student_repo = StudentRepository()
book_repo = BookRepository()
order_repo = OrderRepository()
def get_service():
    return LibraryService(student_repo,book_repo,order_repo)