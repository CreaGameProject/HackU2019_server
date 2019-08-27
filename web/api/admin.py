from django.contrib import admin

from .models import Sound, AlarmTask


@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(AlarmTask)
class AlarmTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'sound', 'sounds_at', 'created_at')
    list_filter = ('sound', 'sounds_at', 'created_at')
    date_hierarchy = 'created_at'
