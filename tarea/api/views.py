from rest_framework import viewsets
from tarea.models import Tarea
from tarea.api.serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset         = Tarea.objects.all()
    serializer_class = TareaSerializer