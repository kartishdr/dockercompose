FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade pip without using rich progress bar (avoids threading issue)
RUN pip install --no-cache-dir --progress-bar off --upgrade pip setuptools wheel

# Install dependencies (again with progress bar off)
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
