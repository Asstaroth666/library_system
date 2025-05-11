from datetime import date
from sqlalchemy.orm import Session
from server.database import SessionLocal
from server.models import User, Book, Borrow
import sys
import os

# Добавляем корневую папку проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

def create_borrow(db: Session, user_id: int, book_id: int, borrow_date: date, return_date: date):
    borrow = Borrow(
        user_id=user_id,
        book_id=book_id,
        borrow_date=borrow_date,
        return_date=return_date
    )
    db.add(borrow)
    db.commit()
    db.refresh(borrow)
    return borrow

def test_create_borrow():
    db = SessionLocal()

    try:
        # 1. Добавляем тестового пользователя
        test_user = User(username="Test User", email="testuser@example.com", password="password")
        db.add(test_user)
        db.commit()  # Сохраняем пользователя в базе данных

        # 2. Добавляем тестовую книгу
        test_book = Book(title="Test Book", author="Author", isbn="123456789", status="available", available_copies=5)
        db.add(test_book)
        db.commit()  # Сохраняем книгу в базе данных

        # 3. Добавляем запись о заимствовании
        borrow_date = date.today()
        return_date = borrow_date  # или позже
        borrow = create_borrow(db, user_id=test_user.id, book_id=test_book.id, borrow_date=borrow_date, return_date=return_date)

        # 4. Проверка
        assert borrow.id is not None
        assert borrow.user_id == test_user.id
        assert borrow.book_id == test_book.id

    finally:
        # 5. Очистка
        db.delete(borrow)
        db.delete(test_book)
        db.delete(test_user)
        db.commit()
        db.close()
