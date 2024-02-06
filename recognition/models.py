from django.db import models
from rest_framework import serializers


# Create your models here.

class AudioFile(models.Model):
    audio = models.FileField(upload_to='media/', blank=True, null=True)
    transcription = models.CharField(max_length=500, blank=True, null=True)


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = "__all__"
        transcription = serializers.CharField(max_length=500, allow_blank=True, required=False)
