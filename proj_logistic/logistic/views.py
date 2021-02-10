from rest_framework import viewsets
from .serializers import LogisticSerializer
from .models import Logistic

class LogisticViewSet(viewsets.ModelViewSet):
    queryset = Logistic.objects.all().order_by('name')
    serializer_class = LogisticSerializer
    