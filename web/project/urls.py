from django.contrib import admin
from django.urls import path

from . import actions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', actions.webhook),
]
