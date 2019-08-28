import os
import uuid

from django.db import models
from django.core.validators import validate_comma_separated_integer_list


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


class HeartRate(models.Model):
    data = models.TextField(validators=[validate_comma_separated_integer_list])
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def split_data(self):
        return [int(i) for i in self.data.split(',')]
