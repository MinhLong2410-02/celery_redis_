# Multi-stage build for efficiency
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Set the timezone to Vietnam
ENV TZ=Asia/Ho_Chi_Minh
RUN ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
    && echo "Asia/Ho_Chi_Minh" > /etc/timezone



WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variables
ENV PYTHONPATH=/app

CMD ["celery", "-A", "app.celery_config", "worker", "--loglevel=info"]