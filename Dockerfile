# Dockerfile for FastAPI with Tesseract OCR and Redis

# Use an official Python runtime as a base image
FROM python:3.10-slim

# Install dependencies including Tesseract
RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-eng poppler-utils && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
