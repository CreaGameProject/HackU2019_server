from rest_framework import viewsets

from .models import AlarmTask, Sound
from .serializer import AlarmTaskSerializer, SoundSerializer


class TaskAlarmViewSet(viewsets.ModelViewSet):
    queryset = AlarmTask.objects.all()
    serializer_class = AlarmTaskSerializer


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer
