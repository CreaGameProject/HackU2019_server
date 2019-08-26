from rest_framework import routers
from .views import TaskAlarmViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskAlarmViewSet)
