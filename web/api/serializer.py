from rest_framework import serializers

from . import models


class AlarmTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlarmTask
        fields = ('sounds_at', 'created_at')


class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeartRate
        fields = ('id', 'data', 'split_data', 'created_at')
