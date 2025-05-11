import requests
from datetime import date
import pdb  # встроенный отладчик

url = "http://127.0.0.1:8001/borrow_book"

payload = {
    "user_id": 1,
    "book_id": 1,
    "borrow_date": str(date.today())
}

# УСТАНАВЛИВАЕМ ТОЧКУ ОСТАНОВА
pdb.set_trace()

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
