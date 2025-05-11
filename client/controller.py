from client import model, api_client, view

class LibraryController:
    def __init__(self):
        self.user = None

    def borrow_book(self, user_id, book_id):
        book = api_client.get_book(book_id)
        if book["available_copies"] > 0:
            api_client.borrow_book(user_id, book_id)
            print("Book borrowed.")
        else:
            print("Book is not available.")

    def return_book(self, borrow_id):
        api_client.return_book(borrow_id)
        print("Book returned.")
