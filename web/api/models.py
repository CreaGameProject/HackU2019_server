from django.db import models
from django.utils import timezone


class AlarmTask(models.Model):
    sound_index = models.IntegerField(default=0)
    sounds_at = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
