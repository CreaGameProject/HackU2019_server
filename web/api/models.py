import os
import uuid

from django.db import models


def upload_to(instance: 'Sound', filename: str):
    filename, ext = os.path.splitext(filename)
    return os.path.join('sound', uuid.uuid4().hex + ext)


class Sound(models.Model):
    file = models.FileField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)


class AlarmTask(models.Model):
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)
    sounds_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
