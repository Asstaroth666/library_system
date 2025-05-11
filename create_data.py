from server.database import SessionLocal
from server.models import Book

# Создание сессии для работы с базой данных
session = SessionLocal()

# Создание книги
new_book = Book(
    title="Amil",
    author="Dota 2 Put' Do Titana",
    isbn="1234567890",
    status="Available",
    available_copies=5
)

# Добавление книги в сессию
session.add(new_book)
session.commit()

# Закрытие сессии
session.close()
