from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "User service is running"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Akhil"},
        {"id": 2, "name": "DevOps Pro"},
    ]
