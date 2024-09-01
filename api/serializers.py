from rest_framework import serializers
from . import models

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upload
        fields = ['file']