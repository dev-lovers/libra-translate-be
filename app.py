from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot as plt
from keras.preprocessing import image
import numpy as np
import requests
import json


app = Flask(__name__)

class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']

URL = "http://iana:8501/v1/models/iana:predict"

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

@app.route('/')
def hello_wordl():
    return { 'message': 'Hello World' }

@app.route('/predict', methods=['POST'])
def predict():
    # Receber a imagem enviada na solicitação POST
    image_file = request.files['image']

    image_path = 'temp_image.jpg'
    image_file.save(image_path)

    prepared_image = prepare_image(image_path, (64, 64))

    predictions = make_prediction(prepared_image)
    for _, pred in enumerate(predictions):
      predicted_class = class_names[np.argmax(pred)]
      print(f"Predicted Value: {predicted_class}")
      return jsonify({'predicted_letter': predicted_class})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
