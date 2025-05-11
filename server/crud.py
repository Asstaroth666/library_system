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
