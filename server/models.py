from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Создание объекта Base, от которого будут наследоваться все модели
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True}  # Добавляем параметр extend_existing

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String)
    status = Column(String)
    available_copies = Column(Integer)

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}  # Добавляем параметр extend_existing

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)

class Borrow(Base):
    __tablename__ = "borrows"
    __table_args__ = {'extend_existing': True}  # Добавляем параметр extend_existing

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    borrow_date = Column(Date)
    return_date = Column(Date)

    user = relationship("User")
    book = relationship("Book")
