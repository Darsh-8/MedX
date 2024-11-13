import os
import pickle
import numpy as np
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ParkinsonInputSerializer

# Load the SVM model and scaler during startup for optimal performance
# Model paths are sourced from environment variables to ensure flexibility
# Update these paths as needed for cloud storage (e.g., Vultr Block Storage or AWS S3)
MODEL_PATH = os.getenv('PARKINSON_MODEL_PATH', 'models/parkinsons_svm_model.pkl')  # Cloud-friendly model path
SCALER_PATH = os.getenv('PARKINSON_SCALER_PATH', 'models/scaler.pkl')

try:
    with open(MODEL_PATH, 'rb') as svm_file:
        svm_model = pickle.load(svm_file)

    with open(SCALER_PATH, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
except Exception as e:
    raise RuntimeError(f"Failed to load model files: {str(e)}")

class ParkinsonPredictionView(APIView):
    def post(self, request):
        # Use the serializer to validate and deserialize input data
        serializer = ParkinsonInputSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated input data as a list
            features = list(serializer.validated_data.values())

            # Add placeholders for the missing features (if required)
            if len(features) == 20:
                features.extend(
                    [0, 0])  # Extend the list with two placeholders

            # Ensure it’s a 2D array for the scaler and model input
            features = np.array([features])  # Model expects a 2D array

            try:
                # Standardize features using the preloaded scaler
                standardized_features = scaler.transform(features)

                # Predict using the SVM model
                prediction = svm_model.predict(standardized_features)
                prediction_text = "Parkinson's Disease" if prediction[0] == 1 else "No Parkinson's Disease"

                # Return the prediction result
                return Response({"prediction": prediction_text}, status=status.HTTP_200_OK)

            except Exception as e:
                # Handle prediction errors, potentially due to model/scaler issues
                return Response(
                    {"error": "An error occurred during prediction", "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        # Return validation errors if the input data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Placeholder: Additional functionalities like logging, monitoring, or custom error handling can be added here
