# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /api

# Copy only requirements first for faster rebuilds
COPY api/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY api/app/ ./app/

# Expose port
EXPOSE 8000

# Run Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]