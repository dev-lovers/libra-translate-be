import json

import numpy as np
import requests
from keras.preprocessing import image
from tensorflow import keras

# iMPORTAR CONFIGURAÇÕES DO ARQUIVO .config
from app.core.config import settings


def prepare_image(img_path, img_size):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array


def make_prediction(instances):
    data = json.dumps(
        {"signature_name": "serving_default", "instances": instances.tolist()}
    )
    headers = {"content-type": "application/json"}
    json_response = requests.post(settings.AI_SERVICE_URL, data=data, headers=headers)
    predictions = json.loads(json_response.text)["predictions"]
    return predictions
