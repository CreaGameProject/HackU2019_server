from django.contrib import admin

from .models import AlarmTask, HeartRate


@admin.register(AlarmTask)
class AlarmTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'sounds_at', 'created_at')
    list_filter = ('sounds_at', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(HeartRate)
class HeartRateAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
