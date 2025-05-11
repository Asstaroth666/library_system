class Book:
    def __init__(self, id, title, author, isbn, status, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
        self.available_copies = available_copies

class User:
    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

class Borrow:
    def __init__(self, id, user_id, book_id, borrow_date, return_date):
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
