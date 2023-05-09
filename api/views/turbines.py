from rest_framework import viewsets

from api.serializers.turbines import (
    OnshoreWindTurbineSerializer,
    OffshoreWindTurbineSerializer,
)
from app.models.turbines import OnshoreWindTurbine, OffshoreWindTurbine


class OnshoreWindTurbineViewSet(viewsets.ModelViewSet):
    queryset = OnshoreWindTurbine.objects.all()
    serializer_class = OnshoreWindTurbineSerializer


class OffshoreWindTurbineViewSet(viewsets.ModelViewSet):
    queryset = OffshoreWindTurbine.objects.all()
    serializer_class = OffshoreWindTurbineSerializer
