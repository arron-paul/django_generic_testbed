from django.core.management import call_command
from django.core.management.base import BaseCommand

from app.fixtures.turbines import wind_turbines
from app.models.turbines import OnshoreWindTurbine, OffshoreWindTurbine


class Command(BaseCommand):
    help = "Flushes existing data and re-creates wind turbines"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--turbines", type=int, help="The amount of wind turbines")

    def handle(self, *args, **options) -> None:
        # Delete all rows in the database
        call_command("flush", interactive=False)

        # Create sensors
        for wind_turbine in wind_turbines():
            if isinstance(wind_turbine, OnshoreWindTurbine):
                pass  # OnshoreWindTurbine.objects.create()
            elif isinstance(wind_turbine, OffshoreWindTurbine):
                pass  # OffshoreWindTurbine.objects.create()
