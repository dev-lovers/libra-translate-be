from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import logging

from .core.config import settings

app = FastAPI()


# ------------------ CÓDIGO AUXILIAR DE PREVISÃO ------------------
import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot as plt
from keras.preprocessing import image
import numpy as np
import requests
import json

class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']

URL = "http://localhost:8501/v1/models/iana:predict"


def prepare_image(img_path, img_size):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0 
    return img_array


def make_prediction(instances):
   data = json.dumps({"signature_name": "serving_default", "instances": instances.tolist()})
   headers = {"content-type": "application/json"}
   json_response = requests.post(URL, data=data, headers=headers)
   predictions = json.loads(json_response.text)['predictions']
   return predictions

# ------------------ X ------------------


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "testing": settings.testing
    }

@app.get("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        # Salvar a imagem temporariamente
        image_path = 'temp_image.jpg'
        with open(image_path, 'wb') as f:
            content = await image.read()
            f.write(content)

        # Preparar a imagem
        prepared_image = prepare_image(image_path, (64, 64))

        # Fazer a previsão
        predictions = make_prediction(prepared_image)

        # Obter as classes previstas
        predicted_classes = [class_names[np.argmax(pred)] for pred in predictions]

        return JSONResponse(content={'predicted_letters': predicted_classes}, status_code=200)

    except KeyError:
        raise HTTPException(status_code=400, detail="Image not found in request")

    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        raise HTTPException(status_code=500, detail=f'Unexpected error: {e}')