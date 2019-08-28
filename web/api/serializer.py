from rest_framework import serializers

from . import models


class AlarmTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlarmTask
        fields = ('sound', 'sounds_at', 'created_at')


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sound
        fields = ('id', 'file', 'created_at')


class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeartRate
        fields = ('id', 'data', 'split_data', 'created_at')
