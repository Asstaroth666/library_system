# 📚 Library Management System

Полнофункциональное клиент-серверное приложение на Python для управления библиотекой, построенное с использованием FastAPI, PostgreSQL и модульной архитектуры.

---

## 🚀 Возможности

- 📖 Добавление, редактирование, удаление и поиск книг
- 👤 Управление пользователями и их действиями
- 📊 Структурированное хранение данных в PostgreSQL
- 🔌 REST API с FastAPI
- ✅ Покрытие кода юнит-тестами (Pytest)
- ⚙️ Миграции базы данных через Alembic
- 🔬 Нагрузочное тестирование с Locust

---

## 📦 Установка и настройка

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 🛠️ Конфигурация базы данных PostgreSQL

1. Создайте базу данных PostgreSQL:

```bash
createdb library
```

2. Настройте строку подключения в `.env` или внутри `settings.py`:

```
DATABASE_URL=postgresql://username:password@localhost:5432/library_db
```

---

## 🏗️ Миграции с Alembic

### Инициализация Alembic (если ещё не сделано)

```bash
alembic init alembic
```

### Создание новой миграции

```bash
alembic revision --autogenerate -m "Initial migration"
```

### Применение миграций

```bash
alembic upgrade head
```

---

## ⚡ Запуск сервера

```bash
uvicorn main:app --reload
```

* `main` — имя Python-файла, где находится экземпляр `FastAPI()`
* `--reload` — автообновление при изменении кода (удобно для разработки)

---

## ✅ Тестирование

### Запуск всех тестов:

```bash
pytest
```

Тесты должны находиться в папке `tests/`, и иметь формат `test_*.py`.

---

## 🔬 Нагрузочное тестирование (Locust)

1. Убедитесь, что установлен Locust:

```bash
pip install locust
```

2. Запуск:

```bash
locust -f locustfile.py
```

3. Перейдите в браузер:
   [http://localhost:8089](http://localhost:8089)

---





