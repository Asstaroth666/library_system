from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

# Модели для данных
class BorrowRequest(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date

class BorrowResponse(BaseModel):
    message: str
    data: BorrowRequest

# Пример маршрута для заимствования книги
@app.post("/borrow_book", response_model=BorrowResponse)
async def borrow_book(borrow_request: BorrowRequest):
    # Здесь должна быть логика для обработки заимствования книги
    # Например, можно добавить запись в базу данных, если все в порядке
    return {"message": "Book borrowed successfully", "data": borrow_request}
