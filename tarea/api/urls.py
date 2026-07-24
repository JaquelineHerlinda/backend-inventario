from rest_framework.routers import DefaultRouter
from tarea.api.views import TareaViewSet

router = DefaultRouter()
router.register('tarea', TareaViewSet, basename='tarea')

urlpatterns = router.urls