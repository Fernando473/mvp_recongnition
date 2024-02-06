from django.urls import path
from .views import *

urlpatterns = [
    path('upload_audio/', recognize_audio, name='upload_audio'),
    path('send_audio/', send_audio, name="send_audio")
]
