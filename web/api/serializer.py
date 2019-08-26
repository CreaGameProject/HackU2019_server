from rest_framework import serializers

from . import models


class AlarmTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AlarmTask
        fields = ('sound_index', 'sounds_at', 'created_at')
