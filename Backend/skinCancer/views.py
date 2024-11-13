import os

import cv2
import numpy as np
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ImageSerializer
from .utils import get_prediction  # Custom function for image prediction

# Define model path using an environment variable for cloud deployment
MODEL_PATH = os.getenv('SKIN_CANCER_MODEL_PATH', 'models/model_resnet50.h5')


# Load model if using a framework like Keras or TensorFlow (ensure memory efficiency)
# from tensorflow.keras.models import load_model
# model = load_model(MODEL_PATH)

class SkinCancer(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Validate input data
            serializer = ImageSerializer(data=request.data)
            if serializer.is_valid():
                # Extract image and convert to OpenCV format
                image = serializer.validated_data['image']
                img_array = np.frombuffer(image.read(), np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                # Validate image format
                if img is None:
                    return Response({
                                        "error": "Invalid image format. Supported formats: JPEG, PNG."},
                                    status=status.HTTP_400_BAD_REQUEST)

                # Predict using a helper function
                label_index, confidence = get_prediction(
                    img)  # Implemented in utils.py
                labels = ['benign', 'malignant']

                # Prepare response
                response_data = {
                    "prediction": labels[label_index],
                    "confidence": confidence
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                # Return validation errors
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle unexpected server errors
            return Response(
                {"error": "Internal server error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Optional: Add logging, monitoring, and error tracking for production, e.g., using Sentry
