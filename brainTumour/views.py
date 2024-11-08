import json
import os

import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Load model once for all requests
MODEL_PATH = os.getenv('MODEL_PATH',
                       'models/optimized_braintumor.h5')  # Update with cloud path if needed
MODEL = load_model(MODEL_PATH)


class BrainTumourPrediction(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        config_file = request.FILES.get('config')

        # Validate the image format
        if not image_file or not image_file.name.lower().endswith(
                ('.jpg', '.jpeg', '.png')):
            return Response({
                                "error": "Invalid image format. Only JPEG and PNG are supported."},
                            status=status.HTTP_400_BAD_REQUEST)

        config = {}
        if config_file:
            try:
                config = json.load(config_file)
            except json.JSONDecodeError:
                return Response(
                    {"error": "Invalid JSON format in config file."},
                    status=status.HTTP_400_BAD_REQUEST)

        try:
            img = Image.open(image_file).convert('RGB')
            resize_dims = config.get('image_preprocessing', {}).get(
                'resize_to', (150, 150))
            img = img.resize(resize_dims)
            img = img_to_array(img) / 255.0
            img = np.expand_dims(img, axis=0)  # Add batch dimension
        except Exception as e:
            return Response({"error": f"Image processing error: {str(e)}"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            prediction = MODEL.predict(img)
            labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor',
                      'pituitary_tumor']
            predicted_class_index = np.argmax(prediction)
            predicted_class = labels[predicted_class_index]
            confidence = float(prediction[0, predicted_class_index])

            confidence_threshold = config.get('model_output', {}).get(
                'confidence_threshold', 0.5)
            if confidence < confidence_threshold:
                return Response(
                    {"error": "Prediction confidence below threshold"},
                    status=status.HTTP_204_NO_CONTENT)

            response_data = {"prediction": predicted_class,
                             "confidence": confidence}
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Prediction error: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
