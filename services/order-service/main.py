from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Order Service"}

@app.get("/orders")
def get_orders():
    # Fetch users from user-service
    try:
        response = httpx.get("http://user-service:8000/users")
        users = response.json()
    except Exception as e:
        users = {"error": str(e)}

    return {
        "orders": ["Order 1", "Order 2"],
        "fetched_users": users
    }
