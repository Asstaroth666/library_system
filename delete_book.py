from server.database import SessionLocal
from server.models import Book, Borrow

def delete_book():
    session = SessionLocal()

    # Показываем все книги перед удалением
    books = session.query(Book).all()
    if not books:
        print("В базе данных нет книг.")
        session.close()
        return

    print("Доступные книги:")
    for book in books:
        print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Доступно: {book.available_copies}")

    # Ввод ID книги для удаления
    try:
        book_id = int(input("\nВведите ID книги, которую хотите удалить: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        session.close()
        return

    # Проверка и удаление заимствований
    borrows = session.query(Borrow).filter_by(book_id=book_id).all()
    if borrows:
        print(f"Найдены {len(borrows)} заимствований для книги с ID {book_id}. Удаляем их...")
        for borrow in borrows:
            session.delete(borrow)
        session.commit()
        print("Все заимствования удалены.")

    # Удаление книги
    book_to_delete = session.query(Book).filter_by(id=book_id).first()
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()
        print(f"Книга с ID {book_id} успешно удалена.")
    else:
        print(f"Книга с ID {book_id} не найдена.")

    session.close()

if __name__ == "__main__":
    delete_book()
