FROM python:3.9.21-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY install.sh . 

COPY ./src ./src

EXPOSE 8000
RUN chmod +x install.sh 
ENTRYPOINT [ "./install.sh" ]
