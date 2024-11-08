import os
import pickle

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HeartAttackPredictionSerializer

# Load the KNN model once at startup, optimizing performance by avoiding repeated loads
# Placeholder: For Vultr Cloud deployment, update 'MODEL_PATH' to reflect the actual cloud storage location
model_path = os.getenv('MODEL_PATH',
                       'models/heart_attack_knn_model.pkl')  # Ensure this is set as an env variable for flexibility
with open(model_path, 'rb') as file:
    knn_model = pickle.load(file)


class HeartAttackPredictionView(APIView):
    def post(self, request):
        # Validate and deserialize input data
        serializer = HeartAttackPredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Prepare input data for prediction
            input_data = [serializer.validated_data[field] for field in
                          serializer.fields]
            input_data = [input_data]  # Reshape to 2D array for model input

            try:
                # Make prediction using the loaded KNN model
                prediction = knn_model.predict(input_data)

                # Interpret prediction: 1 = at risk, 0 = not at risk
                result = prediction[0] == 1

                # Return prediction result
                return Response({"heart_attack": result},
                                status=status.HTTP_200_OK)
            except Exception as e:
                # Handle any model prediction errors
                return Response(
                    {"error": "An error occurred during prediction",
                     "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        # Return validation errors if data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Placeholder: Additional functionalities (e.g., logging or monitoring) can be added here
