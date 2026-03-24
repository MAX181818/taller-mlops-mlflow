FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Fijamos la versión estable 2.10.2
RUN pip install mlflow==2.10.2 psycopg2-binary boto3

EXPOSE 5000
