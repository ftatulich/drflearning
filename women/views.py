from rest_framework import viewsets

from women.models import Woman
from women.serializers import WomanSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer

