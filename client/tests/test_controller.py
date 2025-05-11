import pytest
from client.controller import LibraryController
import sys
import os

# Добавляем корневую папку проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from client.controller import LibraryController

def test_dummy():
    assert True  # просто заглушка


def test_borrow_book_no_copies(monkeypatch, capsys):
    # Имитируем ответ сервера: книга с 0 доступными копиями
    monkeypatch.setattr("client.api_client.get_book", lambda book_id: {"available_copies": 0})

    # Также мокаем вызов borrow_book, чтобы он ничего не делал
    monkeypatch.setattr("client.api_client.borrow_book", lambda user_id, book_id: None)

    ctrl = LibraryController()
    ctrl.borrow_book(user_id=1, book_id=1)

    captured = capsys.readouterr()
    assert "Book is not available" in captured.out
