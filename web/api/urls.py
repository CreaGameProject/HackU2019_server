from rest_framework import routers
from .views import TaskAlarmViewSet, SoundViewSet, HeartRateViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskAlarmViewSet)
router.register('sounds', SoundViewSet)
router.register('heart-rates', HeartRateViewSet)
