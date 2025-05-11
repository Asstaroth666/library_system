from locust import HttpUser, task, between
from datetime import date

class LibraryUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def borrow_book(self):
        self.client.post("/borrow_book", json={
            "user_id": 1,
            "book_id": 1,
            "borrow_date": str(date.today())
        })
