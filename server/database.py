from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # импортируем Base, который содержит все модели

# Создаем подключение к базе данных
DATABASE_URL = "postgresql://postgres:1234@localhost/library"  # Убедись, что здесь правильный URL подключения

# Создание движка базы данных (engine)
engine = create_engine(DATABASE_URL)

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()  # Создаем сессию
    try:
        yield db  # Возвращаем сессию
    finally:
        db.close()  # Закрываем сессию после использования
