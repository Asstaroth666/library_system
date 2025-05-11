import requests

BASE_URL = "http://localhost:8000"

def get_books():
    return requests.get(f"{BASE_URL}/books").json()

def get_book(book_id):
    return requests.get(f"{BASE_URL}/books/{book_id}").json()

def borrow_book(user_id, book_id):
    return requests.post(f"{BASE_URL}/borrow", json={"user_id": user_id, "book_id": book_id})

def return_book(borrow_id):
    return requests.post(f"{BASE_URL}/return", json={"borrow_id": borrow_id})
