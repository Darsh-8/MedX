from rest_framework import serializers


# Serializer for skin cancer prediction input data
class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()  # Validate image file input
    # Add extra fields here if needed
