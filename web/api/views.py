from rest_framework import viewsets

from .models import AlarmTask
from .serializer import AlarmTaskSerializer


class TaskAlarmViewSet(viewsets.ModelViewSet):
    queryset = AlarmTask.objects.all()
    serializer_class = AlarmTaskSerializer
