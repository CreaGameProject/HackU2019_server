from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class AlarmTask(models.Model):
    sounds_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class HeartRate(models.Model):
    data = models.TextField(validators=[validate_comma_separated_integer_list])
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def split_data(self):
        return [int(i) for i in self.data.split(',')]
