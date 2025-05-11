from sqlalchemy.orm import Session
from server.database import SessionLocal
from server.models import Book

# Создаем сессию
session = SessionLocal()

# Получаем все книги из базы
books = session.query(Book).all()

# Выводим информацию о каждой книге
for book in books:
    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {book.status}, Available Copies: {book.available_copies}")

# Закрываем сессию
session.close()
