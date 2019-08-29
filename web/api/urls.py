from rest_framework import routers
from .views import TaskAlarmViewSet, HeartRateViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskAlarmViewSet)
router.register('heart-rates', HeartRateViewSet)
