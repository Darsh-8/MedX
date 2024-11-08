import cv2
import numpy as np
import tensorflow as tf
from keras._tf_keras.keras.applications.resnet50 import preprocess_input

# Load the trained model once when the server starts
MODEL_PATH = 'C:/Users/Darsh Thakkar/GFG Hackathon Models/model_resnet50.h5'
model = tf.keras.models.load_model(MODEL_PATH)


def preprocess_image(img):
    img = cv2.resize(img, (100, 100))
    img = np.expand_dims(img, axis=0)
    return preprocess_input(img)


def get_prediction(img):
    processed_img = preprocess_image(img)
    prediction = model.predict(processed_img)
    label_index = np.argmax(prediction, axis=1)[0]
    confidence = float(prediction[0][label_index])
    return label_index, confidence
