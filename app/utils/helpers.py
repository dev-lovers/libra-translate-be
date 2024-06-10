import json
from typing import List, Tuple

import numpy as np
import requests
from PIL import Image
from tensorflow import keras

from app.core.config import settings


def prepare_image(img_path: str, img_size: Tuple[int, int]) -> np.ndarray:
    img = Image.open(img_path)
    img = img.resize(img_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def make_prediction(instances: List[List[float]]) -> List[float]:
    instances_list = [instance.tolist() for instance in instances]
    data = json.dumps(
        {"signature_name": "serving_default", "instances": instances_list}
    )
    headers = {"content-type": "application/json"}
    json_response = requests.post(settings.AI_SERVICE_URL, data=data, headers=headers)
    predictions = json.loads(json_response.text)["predictions"]
    return predictions
