from server.database import Base, engine  # Импортируем Base и engine из database.py

# Создание всех таблиц, если их еще нет в базе данных
def init_db():
    # Создаем все таблицы, которые описаны в Base
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы в базе данных.")

if __name__ == "__main__":
    init_db()
