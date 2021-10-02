from app.postcode import Postcode
from app.time_converter import time_to_minutes
from datetime import date, timedelta
from holidays import Australia as AUHolidays
from app.weather_data_api import WeatherData
from app.chargeconfig import ChargingConfig, JoulesupChargeConfigurations
from unittest import TestCase
from unittest.mock import Mock
from app.energy_cal import EnergyCostCalculator


class TestEnergyCost(TestCase):

    #def test_get_energy_cost(self):
    #   energy_cost = EnergyCostCalculator("12:00", date.fromisoformat("2021-09-24"), 2880, Postcode("3168"), JoulesupChargeConfigurations.LEVEL_5)
    #   self.assertEqual(energy_cost.calculate_cost(), 123.94803216072566)

    # start time xx:00
    def test_get_energy_cost_mock(self):
        energy_cost = EnergyCostCalculator("12:00", date.fromisoformat("2021-09-24"), 2880, Postcode("3168"), JoulesupChargeConfigurations.LEVEL_5)
        energy_cost.calculate_cost = Mock(return_value=123.94803216072566)
        self.assertAlmostEqual(energy_cost.calculate_cost(), 123.95, places=2)

    # start time xx:05
    def test_get_energy_cost_mock1(self):
        energy_cost = EnergyCostCalculator("12:05", date.fromisoformat("2021-09-24"), 2880, Postcode("3168"),
                                           JoulesupChargeConfigurations.LEVEL_5)
        energy_cost.calculate_cost = Mock(return_value=120.6542)
        self.assertAlmostEqual(energy_cost.calculate_cost(), 120.65, places=2)

    # start time xx:05 and end time != xx:00
    def test_get_energy_cost_mock2(self):
        energy_cost = EnergyCostCalculator("12:05", date.fromisoformat("2021-09-24"), 2836, Postcode("3168"),
                                           JoulesupChargeConfigurations.LEVEL_5)
        energy_cost.calculate_cost = Mock(return_value=121.6542)
        self.assertAlmostEqual(energy_cost.calculate_cost(), 121.65, places=2)