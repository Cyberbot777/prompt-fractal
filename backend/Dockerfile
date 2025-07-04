# Dockerfile

# Use lightweight Python image
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code into container
COPY . .

# Default command to run Iris agent
CMD ["python", "iris_agent.py"]
