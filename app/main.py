import logging

import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from .core.config import settings
from .utils.helpers import make_prediction, prepare_image

app = FastAPI()

class_names = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "I",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "Y",
]

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "testing": settings.testing,
    }


@app.get("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        # Salvar a imagem temporariamente
        image_path = "temp_image.jpg"
        with open(image_path, "wb") as f:
            content = await image.read()
            f.write(content)

        prepared_image = prepare_image(image_path, (64, 64))

        predictions = make_prediction(prepared_image)

        predicted_classes = [class_names[np.argmax(pred)] for pred in predictions]

        return JSONResponse(
            content={"predicted_letters": predicted_classes}, status_code=200
        )

    except KeyError:
        raise HTTPException(status_code=400, detail="Image not found in request")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
