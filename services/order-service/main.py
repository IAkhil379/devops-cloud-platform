from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Order service is running"}

@app.get("/orders")
def get_orders():
    return [
        {"id": 101, "item": "Laptop", "quantity": 1},
        {"id": 102, "item": "Keyboard", "quantity": 2},
    ]
