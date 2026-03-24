import os
import mlflow
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Configurar la conexión a MLflow (usando las credenciales del entorno)
os.environ["MLFLOW_TRACKING_URI"] = "http://mlflow:5000"

app = FastAPI(title="API Inferencia Modelo Taller")

# 2. Definimos cómo deben llegar los datos (nuestras 5 features inventadas)
class Item(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float
    feature_5: float

# Variable global para guardar el modelo
modelo_cargado = None

# 3. Al arrancar la API, descargamos el modelo de MLflow
@app.on_event("startup")
def cargar_modelo():
    global modelo_cargado
    try:
        # Descargamos el modelo registrado con el nombre "Modelo_Taller_RF"
        # Usamos la URI especial de MLflow models:/<nombre>/<estado_o_version>
        print("Descargando modelo desde MLflow...")
        # 'None' indica la versión más reciente
        modelo_cargado = mlflow.pyfunc.load_model(model_uri="models:/Modelo_Taller_RF/None")
        print("✅ Modelo cargado exitosamente")
    except Exception as e:
        print(f"❌ Error al cargar el modelo: {e}")

# 4. El Endpoint para hacer predicciones
@app.post("/predict")
def predict(item: Item):
    if not modelo_cargado:
        return {"error": "El modelo no se cargó correctamente."}
    
    # Convertimos los datos de entrada a un DataFrame de Pandas
    datos = pd.DataFrame([item.dict()])
    
    # Hacemos la predicción
    prediccion = modelo_cargado.predict(datos)
    
    return {
        "prediccion": int(prediccion[0])
    }
