# Use lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (better for caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --progress-bar off -r requirements.txt

# Copy rest of the app code
COPY . .

# Expose app port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
