FROM python:3.10-slim

# Instalamos las librerías necesarias
RUN pip install fastapi uvicorn mlflow==2.10.2 pandas scikit-learn boto3

WORKDIR /app
COPY main.py /app/main.py

EXPOSE 8000

# Comando para correr FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
