from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from server.models import Book, Borrow

# 🔗 Подключение к базе
engine = create_engine("postgresql://postgres:1234@localhost:5432/library")  # замени на свои данные
Session = sessionmaker(bind=engine)
session = Session()

# 📚 Функция выдачи книги
def borrow_book(user_id, book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book and book.available_copies > 0:
        borrow = Borrow(user_id=user_id, book_id=book_id, borrow_date=date.today(), return_date=None)
        session.add(borrow)
        book.available_copies -= 1
        session.commit()
        print("Книга успешно взята.")
    else:
        print("Книга недоступна или не существует.")

def view_borrow_history(user_id):
    borrows = session.query(Borrow).filter_by(user_id=user_id).all()
    if borrows:
        for borrow in borrows:
            # Печать информации о каждой книге
            print(f"Книга ID: {borrow.book_id}, Дата заимствования: {borrow.borrow_date}, Дата возврата: {borrow.return_date}")
    else:
        print("История заимствований пуста.")

from datetime import date

def return_book(user_id, book_id):
    # Ищем активное заимствование книги
    borrow = session.query(Borrow).filter_by(user_id=user_id, book_id=book_id, return_date=None).first()
    
    if borrow:
        borrow.return_date = date.today()  # Устанавливаем дату возврата
        book = session.query(Book).filter_by(id=book_id).first()  # Ищем книгу
        if book:
            book.available_copies += 1  # Увеличиваем количество доступных копий
        session.commit()  # Сохраняем изменения в базе данных
        print("Книга успешно возвращена.")
    else:
        print("Активного заимствования не найдено.")
