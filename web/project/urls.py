from django.contrib import admin
from django.urls import path, include

from api.urls import router as api_router
from . import actions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook', actions.webhook),
    path('api/', include(api_router.urls)),
]
