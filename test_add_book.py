import requests

url = 'http://127.0.0.1:8001/add_book'

book_data = {
    'title': 'Программирование на Python',
    'author': 'Иван Иванов',
    'isbn': '1234567890',  # Пример корректного ISBN
    'status': 'Available',
    'available_copies': 10
}

try:
    response = requests.post(url, json=book_data)
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
