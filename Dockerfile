# Use a small official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirement file and install deps (pytest)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application and tests into the image
COPY analyzer.py test_analyzer.py .

# When container runs, run pytest
CMD ["pytest", "-q"]
