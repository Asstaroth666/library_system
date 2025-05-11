from server.database import SessionLocal, get_db

from server.models import Book

def create_book(title, author, isbn, status, available_copies):
    # Получаем сессию
    db = next(get_db())

    # Создаем объект книги
    new_book = Book(
        title=title,
        author=author,
        isbn=isbn,
        status=status,
        available_copies=available_copies
    )

    # Добавляем книгу в сессию
    db.add(new_book)
    db.commit()  # Сохраняем изменения
    db.refresh(new_book)  # Обновляем объект, чтобы получить его id
    return new_book

# Пример использования
book = create_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "available", 5)
print(f"Book created: {book.title}, ID: {book.id}")
