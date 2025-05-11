from server.database import SessionLocal
from server.models import Book

def create_book():
    # Ввод данных о книге с использованием input()
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    isbn = input("Введите ISBN книги: ")
    status = input("Введите статус книги (например, 'Available'): ")
    available_copies = int(input("Введите количество доступных копий: "))

    # Создание сессии для работы с базой данных
    session = SessionLocal()

    # Создание книги с введенными данными
    new_book = Book(
        title=title,
        author=author,
        isbn=isbn,
        status=status,
        available_copies=available_copies
    )

    # Добавление книги в сессию
    session.add(new_book)
    session.commit()

    # Закрытие сессии
    session.close()

    print(f"Книга '{title}' успешно добавлена в библиотеку!")

# Вызов функции для создания книги
if __name__ == "__main__":
    create_book()
