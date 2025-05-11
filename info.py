from server.database import SessionLocal
from server.models import Book, User, Borrow
from sqlalchemy.orm import Session

# Функция для отображения списка книг
def view_books():
    session = SessionLocal()
    try:
        books = session.query(Book).all()

        if books:
            print("Список книг:")
            for book in books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Статус: {book.status}, Доступно: {book.available_copies}")
        else:
            print("В базе данных нет книг.")
    except Exception as e:
        print(f"Ошибка при получении списка книг: {e}")
    finally:
        session.close()

# Функция для отображения списка пользователей
# Функция для отображения списка пользователей
def view_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()

        if users:
            print("Список пользователей:")
            for user in users:
                print(f"ID: {user.id}, Имя: {user.username}, Email: {user.email}")  # Используем user.username вместо user.name
        else:
            print("В базе данных нет пользователей.")
    except Exception as e:
        print(f"Ошибка при получении списка пользователей: {e}")
    finally:
        session.close()


# Функция для отображения списка заимствований
def view_borrows():
    session = SessionLocal()
    try:
        borrows = session.query(Borrow).all()

        if borrows:
            print("Список заимствований:")
            for borrow in borrows:
                print(f"ID Заимствования: {borrow.id}, Пользователь ID: {borrow.user_id}, Книга ID: {borrow.book_id}, Дата заимствования: {borrow.borrow_date}")
        else:
            print("В базе данных нет заимствований.")
    except Exception as e:
        print(f"Ошибка при получении списка заимствований: {e}")
    finally:
        session.close()

# Главная функция для меню
def main_menu():
    while True:
        print("\nДобро пожаловать в систему библиотеки!")
        print("1. Посмотреть все книги")
        print("2. Посмотреть всех пользователей")
        print("3. Посмотреть все заимствования")
        print("4. Выйти")
        
        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")
            continue

        if choice == 1:
            view_books()
        elif choice == 2:
            view_users()
        elif choice == 3:
            view_borrows()
        elif choice == 4:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
