from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Исправляем модель User (убираем дублирование)
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Book(Base):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True}  # Добавляем параметр extend_existing

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String)
    status = Column(String)
    available_copies = Column(Integer)


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
