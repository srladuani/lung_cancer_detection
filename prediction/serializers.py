from rest_framework import serializers
from .models import XrayImage

class XrayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = XrayImage
        fields = ['id', 'image', 'prediction', 'uploaded_at']
