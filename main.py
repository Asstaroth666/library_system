from logic import borrow_book, return_book, view_borrow_history

def main():
    print("Добро пожаловать в систему библиотеки!")
    print("1. Взять книгу")
    print("2. Вернуть книгу")
    print("3. Просмотреть историю заимствований")
    choice = input("Выберите действие: ")

    user_id = int(input("Введите ваш ID пользователя: "))
    
    if choice == "1":
        book_id = int(input("Введите ID книги, которую хотите взять: "))
        borrow_book(user_id, book_id)
    elif choice == "2":
        book_id = int(input("Введите ID книги, которую хотите вернуть: "))
        return_book(user_id, book_id)
    elif choice == "3":
        view_borrow_history(user_id)
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()

