import subprocess

import whisper
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AudioFile, AudioSerializer


@api_view(['POST'])
def recognize_audio(request):
    try:
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            update_file = AudioFile.objects.get(pk=file.pk)

            file_instance = update_file.audio
            # text = transcribe_audio(file_instance.path)
            model = whisper.load_model("base")
            filename = file_instance.path
            result = model.transcribe(filename)
            text = result["text"]
            update_file.transcription = text
            update_file.save()
            data = AudioSerializer(update_file).data

            return Response({"message": "Transcription created successfully", "audio": data},
                            status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def send_audio(request):
    return render(request, 'send_audio.html')
