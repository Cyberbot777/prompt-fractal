# Use lightweight Python base
FROM python:3.11-slim

# Set environment to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install system packages needed to build psycopg[binary]
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Default to sleep so container stays up during dev
CMD ["tail", "-f", "/dev/null"]
