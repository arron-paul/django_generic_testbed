from django.db.models import (
    Model,
    Manager,
    BigAutoField,
    CharField,
    FloatField,
    OneToOneField,
    CASCADE,
)

from app.models.coordinates import Coordinate


class WindTurbine(Model):
    """
    Abstract model for wind turbines.
    Includes common fields for all wind turbines
    """

    objects: Manager = Manager()
    id: BigAutoField = BigAutoField(primary_key=True)
    manufacturer: CharField = CharField(max_length=100)
    model: CharField = CharField(max_length=100)
    height: FloatField = FloatField()
    rotor_diameter: FloatField = FloatField()
    coordinates: OneToOneField = OneToOneField(Coordinate, on_delete=CASCADE)

    class Meta:
        abstract = True


class OnshoreWindTurbine(WindTurbine):
    """
    Concrete model for onshore wind turbines.
    Includes additional fields for onshore wind turbines
    """

    objects: Manager = Manager()
    id: BigAutoField = BigAutoField(primary_key=True)
    blade_length: FloatField = FloatField()
    hub_height: FloatField = FloatField()
    cut_in_wind_speed: FloatField = FloatField()
    rated_wind_speed: FloatField = FloatField()
    cut_out_wind_speed: FloatField = FloatField()


class OffshoreWindTurbine(WindTurbine):
    """
    Concrete model for offshore wind turbines.
    Includes additional fields for offshore wind turbines
    """

    objects: Manager = Manager()
    id: BigAutoField = BigAutoField(primary_key=True)
    foundation_type: CharField = CharField(max_length=100)
    water_depth: FloatField = FloatField()
    distance_to_shore: FloatField = FloatField()
    rated_output: FloatField = FloatField()
