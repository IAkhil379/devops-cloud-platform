from fastapi import FastAPI, HTTPException
import httpx

from models import User
from database import Base, engine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"status": "User Service Running"}

# ✅ Internal call to order-service
@app.get("/orders-from-order-service")
async def get_orders():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://order-service:8001/orders")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Failed to contact order-service: {e}")
