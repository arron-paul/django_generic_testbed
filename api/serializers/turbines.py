from rest_framework import serializers

from api.serializers.coordinates import CoordinateSerializer
from app.models.turbines import WindTurbine, OnshoreWindTurbine, OffshoreWindTurbine


class WindTurbineSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer()

    class Meta:
        model = WindTurbine
        fields = "__all__"
        abstract = True


class OnshoreWindTurbineSerializer(WindTurbineSerializer):
    class Meta(WindTurbineSerializer.Meta):
        model = OnshoreWindTurbine


class OffshoreWindTurbineSerializer(WindTurbineSerializer):
    class Meta(WindTurbineSerializer.Meta):
        model = OffshoreWindTurbine
