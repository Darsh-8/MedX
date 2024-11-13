from rest_framework import serializers


# Serializer to validate and deserialize input data for Heart Attack prediction
class HeartAttackPredictionSerializer(serializers.Serializer):
    age = serializers.FloatField()
    sex = serializers.IntegerField()
    cp = serializers.IntegerField()  # Chest pain type (0-3)
    trtbps = serializers.FloatField()  # Resting blood pressure
    chol = serializers.FloatField()  # Serum cholesterol level
    fbs = serializers.IntegerField()  # Fasting blood sugar (0 or 1)
    restecg = serializers.IntegerField()  # Resting electrocardiographic results (0-2)
    thalachh = serializers.FloatField()  # Maximum heart rate achieved
    exng = serializers.IntegerField()  # Exercise-induced angina (0 or 1)
    oldpeak = serializers.FloatField()  # Depression induced by exercise
    slp = serializers.IntegerField()  # Slope of peak exercise ST segment (0-2)
    caa = serializers.IntegerField()  # Number of major vessels colored by fluoroscopy (0-3)
    thall = serializers.IntegerField()  # Thalassemia (1-3)

    # Placeholder: Define any additional fields or validation rules here, if required
