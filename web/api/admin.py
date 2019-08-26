from django.contrib import admin
from . import models


@admin.register(models.AlarmTask)
class AlarmTaskAdmin(admin.ModelAdmin):
    pass
