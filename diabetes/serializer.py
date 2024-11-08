from rest_framework import serializers


# Serializer for validating input data for Diabetes prediction
class DiabetesPredictionSerializer(serializers.Serializer):
    Pregnancies = serializers.IntegerField(min_value=0)
    Glucose = serializers.IntegerField(min_value=0)
    BloodPressure = serializers.IntegerField(min_value=0)
    SkinThickness = serializers.IntegerField(min_value=0)
    Insulin = serializers.IntegerField(min_value=0)
    BMI = serializers.FloatField(min_value=0.0)
    DiabetesPedigreeFunction = serializers.FloatField(min_value=0.0)
    Age = serializers.IntegerField(min_value=0)

    # Placeholder: Add more fields or validation rules here as needed.
