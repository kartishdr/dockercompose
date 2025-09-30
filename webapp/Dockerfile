FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies (no pip upgrade to avoid thread issues)
RUN pip install --no-cache-dir --progress-bar=off -r requirements.txt

COPY . .

CMD ["python", "app.py"]


