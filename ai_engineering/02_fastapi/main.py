from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome to home route"}

@app.get("/books")
def get_books():
    return {
        "data": [
            "Python Book",
            "Backend Book",
            "System Design Book"
        ]
    }


@app.post("/books")
def create_book():
    return {"message": "Book created"}


@app.put("/books/{book_id}")
def update_book(book_id: int):
    return {"message": f"Book title updated with id: {book_id}"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return {"message": f"Book deleted id no: {book_id}"}
