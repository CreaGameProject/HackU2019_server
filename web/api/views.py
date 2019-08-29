from rest_framework import viewsets

from .models import AlarmTask, Sound, HeartRate
from .serializer import AlarmTaskSerializer, SoundSerializer, HeartRateSerializer


class TaskAlarmViewSet(viewsets.ModelViewSet):
    queryset = AlarmTask.objects.all()
    serializer_class = AlarmTaskSerializer


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer


class HeartRateViewSet(viewsets.ModelViewSet):
    queryset = HeartRate.objects.all()
    serializer_class = HeartRateSerializer
