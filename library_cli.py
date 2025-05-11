from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.models import Base, User, Book, Borrow

# Создаем подключение к базе данных
DATABASE_URL = "postgresql://postgres:1234@localhost/library"  # Убедись, что здесь правильный URL подключения

# Создание движка базы данных (engine)
engine = create_engine(DATABASE_URL)

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция для регистрации нового пользователя
def register_user(db):
    print("Регистрация нового пользователя:")
    username = input("Введите ваше имя: ")
    email = input("Введите ваш email: ")
    password = input("Введите ваш пароль: ")
    
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"Пользователь {username} успешно зарегистрирован! Ваш ID: {new_user.id}")
    return new_user.id

# Функция для входа пользователя
def login_user(db):
    attempts = 0  # Счетчик неудачных попыток
    while attempts < 3:
        user_id = int(input("Введите ваш ID: "))
        user = db.query(User).filter(User.id == user_id).first()
        
        if user:
            print(f"Добро пожаловать, {user.username}!")
            return user.id
        else:
            attempts += 1
            print(f"Пользователь с таким ID не найден. Попробуйте снова. Осталось попыток: {3 - attempts}")
    
    print("Слишком много неудачных попыток. Попробуйте позже.")
    return None

# Функция для получения книги
def borrow_book(db, user_id):
    print("\nДоступные книги:")
    books = db.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Доступно: {book.available_copies}")

    book_id = int(input("\nВведите ID книги, которую хотите взять: "))
    borrow_date = datetime.now().date()
    
    # Проверка на наличие книги
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        if book.available_copies > 0:  # Если есть доступные экземпляры
            borrow_entry = Borrow(user_id=user_id, book_id=book_id, borrow_date=borrow_date)
            db.add(borrow_entry)
            
            # Уменьшаем количество доступных экземпляров книги
            book.available_copies -= 1
            db.commit()
            db.refresh(borrow_entry)
            print(f"Вы успешно взяли книгу: {book.title}")
        else:
            print(f"Книга {book.title} в данный момент недоступна для заимствования.")
    else:
        print("Такой книги не существует.")


# Функция для возврата книги
def return_book(db, user_id):
    print("\nВаши заимствованные книги:")
    borrows = db.query(Borrow).filter(Borrow.user_id == user_id).all()

    if not borrows:
        print("У вас нет заимствованных книг.")
        return

    for borrow in borrows:
        book = db.query(Book).filter(Book.id == borrow.book_id).first()
        print(f"ID заимствования: {borrow.id}, Название книги: {book.title}")

    borrow_id = int(input("\nВведите ID заимствования для возврата: "))
    borrow_entry = db.query(Borrow).filter(Borrow.id == borrow_id, Borrow.user_id == user_id).first()

    if borrow_entry:
        book = db.query(Book).filter(Book.id == borrow_entry.book_id).first()
        if book:
            book.available_copies += 1  # Увеличиваем доступные копии
        db.delete(borrow_entry)
        db.commit()
        print("Вы успешно вернули книгу!")
    else:
        print("Вы не заимствовали книгу с таким ID.")


# Функция для просмотра истории заимствований
def view_borrow_history(db, user_id):
    print("\nВаша история заимствований:")
    borrows = db.query(Borrow).filter(Borrow.user_id == user_id).all()
    for borrow in borrows:
        book = db.query(Book).filter(Book.id == borrow.book_id).first()
        print(f"ID книги: {book.id}, Название: {book.title}, Дата взятия: {borrow.borrow_date}")

# Основной цикл
def main():
    db = next(get_db())
    
    print("Добро пожаловать в систему библиотеки!")
    action = input("1. Зарегистрироваться\n2. Войти\nВыберите действие (1 или 2): ")

    user_id = None
    if action == "1":
        user_id = register_user(db)
    elif action == "2":
        # Пытаемся войти в систему
        user_id = login_user(db)
    else:
        print("Неверный выбор.")
        return

    if not user_id:
        print("Выход из программы.")
        return

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Взять книгу")
        print("2. Вернуть книгу")
        print("3. Просмотреть историю заимствований")
        print("4. Выход")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            borrow_book(db, user_id)
        elif choice == "2":
            return_book(db, user_id)
        elif choice == "3":
            view_borrow_history(db, user_id)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
