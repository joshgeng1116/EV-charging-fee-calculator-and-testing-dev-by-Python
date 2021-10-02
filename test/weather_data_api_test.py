from datetime import date
from unittest import TestCase
import requests
import unittest
from app.postcode import Postcode
from app.weather_data_api import WeatherData
from unittest.mock import Mock
from app.time_converter import time_to_minutes


class WeatherDataTest(TestCase):

    def test_get_id(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        weather_data.get_weather_data_by_id = Mock(return_value="dac1a3a1-3ea5-4215-a073-3348d53b518f")
        self.assertEqual(weather_data.get_weather_data_by_id(), "dac1a3a1-3ea5-4215-a073-3348d53b518f")

    def test_cannot_get_id(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        weather_data.get_weather_data_by_id = Mock(return_value=None)
        self.assertEqual(weather_data.get_weather_data_by_id(), None)

    def test(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_location_id(), "dac1a3a1-3ea5-4215-a073-3348d53b518f")
