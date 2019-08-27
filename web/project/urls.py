from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from api.urls import router as api_router
from . import actions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook', actions.webhook),
    path('api/', include(api_router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
