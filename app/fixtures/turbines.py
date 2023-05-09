import random
from dataclasses import dataclass
from typing import List, Tuple, Union


@dataclass
class WindTurbineFixture:
    manufacturer: str
    model: str
    height: float
    rotor_diameter: float

    @staticmethod
    def model_options() -> List[str]:
        return [
            "Horizontal Axis",
            "Vertical Axis",
            "Upwind",
            "Downwind",
            "Darrieus",
            "Savonius",
        ]

    @staticmethod
    def manufacturer_options() -> List[str]:
        return [
            "Vestas",
            "Siemens Gamesa",
            "General Electric",
            "Nordex",
            "Enercon",
            "Goldwind",
        ]

    @staticmethod
    def height_options() -> Tuple[float, float]:
        return 10, 200

    @staticmethod
    def rotor_diameter_options() -> Tuple[float, float]:
        return 60, 160

    class Meta:
        abstract = True


@dataclass
class OnshoreWindTurbineFixture(WindTurbineFixture):
    blade_length: float
    hub_height: float
    cut_in_wind_speed: float
    cut_out_wind_speed: float
    rated_wind_speed: float

    @staticmethod
    def blade_length_options() -> Tuple[float, float]:
        return 60, 100

    @staticmethod
    def hub_height_options() -> Tuple[float, float]:
        return 20, 200

    @staticmethod
    def cut_in_wind_speed_options() -> Tuple[float, float]:
        return 3, 15

    @staticmethod
    def cut_out_wind_speed_options() -> Tuple[float, float]:
        return 20, 35

    @staticmethod
    def rated_wind_speed_options() -> Tuple[float, float]:
        return 10, 20


@dataclass
class OffshoreWindTurbineFixture(WindTurbineFixture):
    foundation_type: str
    water_depth: float
    distance_to_shore: float
    rated_output: float

    @staticmethod
    def foundation_type_options() -> List[str]:
        return ["Monopile", "Jacket", "Gravity Base", "Floating"]

    @staticmethod
    def water_depth_options() -> Tuple[float, float]:
        return 10, 100

    @staticmethod
    def distance_to_shore_options() -> Tuple[float, float]:
        return 10, 100

    @staticmethod
    def rated_output_options() -> Tuple[float, float]:
        return 3, 12


def wind_turbines(
    num: int,
) -> List[Union[OnshoreWindTurbineFixture, OffshoreWindTurbineFixture]]:
    """
    Create a number of onshore and offshore wind turbine fixtures
    """
    num_onshore_turbines: int = random.randint(1, num)
    num_offshore_turbines: int = num_onshore_turbines - num_onshore_turbines
    return [
        *onshore_wind_turbines(num_onshore_turbines),
        *offshore_wind_turbines(num_offshore_turbines),
    ]


def onshore_wind_turbines(num: int) -> List[OnshoreWindTurbineFixture]:
    """
    Create a number of onshore wind turbine fixtures
    """
    onshore_wind_turbines: List[OnshoreWindTurbineFixture] = []
    for i in range(num):
        manufacturer: str = random.choice(WindTurbineFixture.manufacturer_options())
        model: str = random.choice(WindTurbineFixture.model_options())
        height: float = random.uniform(*WindTurbineFixture.height_options())
        rotor_diameter: float = random.uniform(
            *WindTurbineFixture.rotor_diameter_options()
        )
        blade_length: float = random.uniform(
            *OnshoreWindTurbineFixture.blade_length_options()
        )
        hub_height: float = random.uniform(
            *OnshoreWindTurbineFixture.hub_height_options()
        )
        cut_in_wind_speed: float = random.uniform(
            *OnshoreWindTurbineFixture.cut_in_wind_speed_options()
        )
        cut_out_wind_speed: float = random.uniform(
            *OnshoreWindTurbineFixture.cut_out_wind_speed_options()
        )
        rated_wind_speed: float = random.uniform(
            *OnshoreWindTurbineFixture.rated_wind_speed_options()
        )
        onshore_wind_turbines.append(
            OnshoreWindTurbineFixture(
                manufacturer,
                model,
                height,
                rotor_diameter,
                blade_length,
                hub_height,
                cut_in_wind_speed,
                cut_out_wind_speed,
                rated_wind_speed,
            )
        )
    return onshore_wind_turbines


def offshore_wind_turbines(num: int) -> List[OffshoreWindTurbineFixture]:
    """
    Create a number of offshore wind turbine fixtures
    """
    offshore_wind_turbines: List[OffshoreWindTurbineFixture] = []
    for i in range(num):
        manufacturer: str = random.choice(WindTurbineFixture.manufacturer_options())
        model: str = random.choice(WindTurbineFixture.model_options())
        height: float = random.uniform(*WindTurbineFixture.height_options())
        rotor_diameter: float = random.uniform(
            *WindTurbineFixture.rotor_diameter_options()
        )
        foundation_type: str = random.choice(
            OffshoreWindTurbineFixture.foundation_type_options()
        )
        water_depth: float = random.uniform(
            *OffshoreWindTurbineFixture.water_depth_options()
        )
        distance_to_shore: float = random.uniform(
            *OffshoreWindTurbineFixture.distance_to_shore_options()
        )
        rated_output: float = random.uniform(
            *OffshoreWindTurbineFixture.rated_output_options()
        )
        offshore_wind_turbines.append(
            OffshoreWindTurbineFixture(
                manufacturer,
                model,
                height,
                rotor_diameter,
                foundation_type,
                water_depth,
                distance_to_shore,
                rated_output,
            )
        )
    return offshore_wind_turbines
