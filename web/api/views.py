from rest_framework import viewsets

from .models import AlarmTask, HeartRate
from .serializer import AlarmTaskSerializer, HeartRateSerializer


class TaskAlarmViewSet(viewsets.ModelViewSet):
    queryset = AlarmTask.objects.all()
    serializer_class = AlarmTaskSerializer


class HeartRateViewSet(viewsets.ModelViewSet):
    queryset = HeartRate.objects.all()
    serializer_class = HeartRateSerializer
