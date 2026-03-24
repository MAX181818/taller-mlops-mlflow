FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Fijamos la misma versión de mlflow aquí
RUN pip install jupyterlab mlflow==2.10.2 psycopg2-binary boto3 pandas scikit-learn

WORKDIR /workspace
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
