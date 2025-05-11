import sys
import os
from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context
from server.models import Base  # Здесь должен быть импорт Base, который содержит все ваши модели

# Добавляем путь к проекту, чтобы Alembic мог найти модули
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# Настройка логирования
fileConfig(context.config.config_file_name)

# Получаем строку подключения из конфигурации Alembic
config = context.config
target_metadata = Base.metadata  # Подключаем метаданные для миграции

# Функция для подключения к базе данных
def get_url():
    return config.get_main_option("sqlalchemy.url")

# Функция для подключения к базе данных
def run_migrations_offline():
    """Запуск миграций в режиме оффлайн."""
    url = get_url()
    context.configure(url=url, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в режиме онлайн."""
    connectable = create_engine(get_url(), poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# Основная логика: запуск миграции в оффлайн или онлайн режиме
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
