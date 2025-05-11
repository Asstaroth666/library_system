from server.database import SessionLocal
from server.models import Book, Borrow

def delete_book():
    # Ввод данных для удаления книги
    book_id = int(input("Введите ID книги, которую хотите удалить: "))
    
    # Создание сессии для работы с базой данных
    session = SessionLocal()

    # Проверим, есть ли заимствования этой книги
    borrows = session.query(Borrow).filter_by(book_id=book_id).all()

    # Если есть заимствования, удалим их
    if borrows:
        print(f"Найдены {len(borrows)} заимствований для книги с ID {book_id}. Удаляем их...")
        for borrow in borrows:
            session.delete(borrow)  # Удаляем все заимствования этой книги
        session.commit()
        print("Все заимствования удалены.")

    # Теперь удалим саму книгу
    book_to_delete = session.query(Book).filter_by(id=book_id).first()

    # Если книга найдена
    if book_to_delete:
        session.delete(book_to_delete)  # Удаляем книгу
        session.commit()
        print(f"Книга с ID {book_id} успешно удалена.")
    else:
        print(f"Книга с ID {book_id} не найдена.")

    # Закрытие сессии
    session.close()

# Вызов функции для удаления книги
if __name__ == "__main__":
    delete_book()
