

def borrow_book(user_id: int, book_id: int, borrow_date: str):
    # Пример: заглушка логики
    print(f"User {user_id} borrowed book {book_id} on {borrow_date}")
    return {"message": "Book borrowed successfully"}

def return_book(user_id: int, book_id: int, return_date: str):
    print(f"User {user_id} returned book {book_id} on {return_date}")
    return {"message": "Book returned successfully"}

def view_borrow_history(user_id: int):
    return {"history": []}

