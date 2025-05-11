from fastapi import FastAPI
from pydantic import BaseModel
from logic import borrow_book, return_book, view_borrow_history

app = FastAPI()

# Модели для запросов
class BorrowRequest(BaseModel):
    user_id: int
    book_id: int

@app.post("/borrow_book")
async def borrow_book_route(borrow_request: BorrowRequest):
    result = borrow_book(borrow_request.user_id, borrow_request.book_id)
    return {"message": result}

@app.post("/return_book")
async def return_book_route(borrow_request: BorrowRequest):
    result = return_book(borrow_request.user_id, borrow_request.book_id)
    return {"message": result}

@app.get("/view_borrow_history/{user_id}")
async def view_borrow_history_route(user_id: int):
    result = view_borrow_history(user_id)
    return {"history": result}

# Удаляем основной цикл, так как FastAPI будет управлять сервером
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
