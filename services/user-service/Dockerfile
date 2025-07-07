# 1. Use official Python image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy everything from current folder into /app in the container
COPY . /app

# 4. Upgrade pip and install FastAPI + Uvicorn
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

# 5. Expose port 8000 to access the app
EXPOSE 8000

# 6. Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
