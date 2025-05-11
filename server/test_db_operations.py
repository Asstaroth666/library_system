from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.models import Base, Borrow
from server.database import engine

# Настроим сессию SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для тестирования записи в базу данных
def create_borrow(db, user_id: int, book_id: int, borrow_date: date, return_date: date):
    new_borrow = Borrow(user_id=user_id, book_id=book_id, borrow_date=borrow_date, return_date=return_date)
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)
    return new_borrow

def test_create_borrow():
    db = SessionLocal()  # Создаем сессию для работы с БД

    # Тестовые данные
    user_id = 1  # Здесь будет id пользователя, который берет книгу
    book_id = 1  # Здесь будет id книги, которую берет пользователь
    borrow_date = date.today()  # Текущая дата
    return_date = date.today()  # Например, та же дата для возврата

    # Вызываем функцию для создания записи
    borrow = create_borrow(db, user_id, book_id, borrow_date, return_date)

    # Проверяем, что запись добавилась
    print(f"Borrow record created: ID={borrow.id}, Borrow Date={borrow.borrow_date}, Return Date={borrow.return_date}")

    db.close()  # Закрываем сессию после выполнения

# Запуск теста
test_create_borrow()
