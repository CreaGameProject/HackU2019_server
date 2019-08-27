from rest_framework import routers
from .views import TaskAlarmViewSet, SoundViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskAlarmViewSet)
router.register('sounds', SoundViewSet)
