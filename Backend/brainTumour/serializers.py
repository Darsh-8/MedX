from rest_framework import serializers

from .models import BrainTumourImage


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrainTumourImage
        fields = ['image', 'uploaded_at']
