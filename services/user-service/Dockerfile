FROM python:3.11-slim

WORKDIR /app

# ✅ Install netcat properly
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "postgres", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
