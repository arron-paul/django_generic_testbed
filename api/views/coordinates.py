from rest_framework import viewsets

from api.serializers.coordinates import CoordinateSerializer
from app.models.coordinates import Coordinate


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
