from django.utils import timezone
from django.contrib.gis.db.models import PointField
from django.db.models import Model, FloatField, DateTimeField, Manager, BigAutoField


class Coordinate(Model):
    """
    Concrete model for GPS coordinates
    """

    objects: Manager = Manager()
    id: BigAutoField = BigAutoField(primary_key=True)
    location: PointField = PointField()
    altitude: FloatField = FloatField(null=True, blank=True)
    accuracy: FloatField = FloatField(null=True, blank=True)
    last_updated: DateTimeField = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        When GPS coordinates are updated, update the last_updated datetime
        """
        self.last_updated = timezone.now()
        super().save(*args, **kwargs)
