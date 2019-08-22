from django.contrib import admin
from django.urls import path

from . import skills

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', skills.skill_view),
]
