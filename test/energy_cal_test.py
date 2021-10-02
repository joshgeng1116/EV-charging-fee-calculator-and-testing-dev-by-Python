from app.postcode import Postcode
from app.time_converter import time_to_minutes
from datetime import date, timedelta
from holidays import Australia as AUHolidays
from app.weather_data_api import WeatherData
from app.chargeconfig import ChargingConfig, JoulesupChargeConfigurations
from unittest import TestCase
from app.energy_cal import EnergyCostCalculator


class TestEnergyCost(TestCase):

    def test_get_energy_cost(self):
        energy_cost = EnergyCostCalculator("12:00", date.fromisoformat("2021-09-24"), 2880, Postcode("3168"), JoulesupChargeConfigurations.LEVEL_5)
        self.assertEqual(energy_cost.calculate_cost(), 123.94803216072566)
