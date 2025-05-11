from locust import HttpUser, task, between
from datetime import date

class LibraryUser(HttpUser):
    wait_time = between(1, 2)  # Время между запросами
    host = "http://localhost:8000"  # Адрес FastAPI сервера

    @task
    def borrow_book(self):
        # Запрос на заимствование книги
        response = self.client.post("/borrow_book", json={
            "user_id": 1,
            "book_id": 1,
            "borrow_date": str(date.today())
        })

        # Печать ответа на консоль для отладки
        print(f"Response: {response.status_code}, {response.json()}")
        assert response.status_code == 200  # Убедитесь, что получен статус 200

    @task
    def another_task(self):
        # Дополнительный запрос для тестирования, если нужно
        pass

@task
def borrow_book(self):
    response = self.client.post("/borrow_book", json={
        "user_id": 1,
        "book_id": 1,
        "borrow_date": str(date.today())
    })
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    assert response.status_code == 200  # Убедитесь, что получен статус 200