import os
import pickle

import numpy as np
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import DiabetesPredictionSerializer

# Set model path via environment variable for flexibility
# Placeholder: Update model_path for cloud storage if using Vultr Object Storage or similar
model_path = os.getenv('MODEL_PATH', 'models/svm_diabetes_model.pkl')
with open(model_path, 'rb') as f:
    classifier = pickle.load(f)
    scaler = pickle.load(f)


class DiabetesPredictionView(APIView):
    def post(self, request):
        # Use the serializer to validate and deserialize input data
        serializer = DiabetesPredictionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            features = [
                data['Pregnancies'],
                data['Glucose'],
                data['BloodPressure'],
                data['SkinThickness'],
                data['Insulin'],
                data['BMI'],
                data['DiabetesPedigreeFunction'],
                data['Age']
            ]

            # Prepare input data for prediction
            input_data = np.array(features).reshape(1, -1)
            standardized_data = scaler.transform(input_data)

            # Predict with the loaded classifier
            try:
                prediction = classifier.predict(standardized_data)
                result = {"prediction": int(prediction[0])}
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                # Handle prediction errors gracefully
                return Response(
                    {"error": "Error occurred during prediction.",
                     "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            # Return validation errors
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

# Placeholder: Additional logic for logging, metrics, or data storage could be added here.
