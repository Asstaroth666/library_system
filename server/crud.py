# crud.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models

def register_user(db: Session, username: str, email: str, password: str):
    # Проверяем, существует ли уже пользователь с таким email
    existing_user = db.query(models.User).filter(models.User.email == email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    # Если email свободен, создаем нового пользователя
    new_user = models.User(username=username, email=email, password=password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Обновляем объект, чтобы получить id
    
    return new_user



def get_books(db):
    return db.query(models.Book).all()

def create_borrow(db, data):
    book = db.query(models.Book).filter_by(id=data.book_id).first()
    if book.available_copies == 0:
        raise HTTPException(400, "No copies available")
    book.available_copies -= 1
    borrow = models.Borrow(user_id=data.user_id, book_id=data.book_id)
    db.add(borrow)
    db.commit()
