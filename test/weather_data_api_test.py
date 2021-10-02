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
        self.assertEqual(weather_data.get_location_id(), "dac1a3a1-3ea5-4215-a073-3348d53b518f")

    def test_get_weather_data(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_weather_data_by_id(), (4.4, "06:41", "17:58", 18, 11.283333333333333))

    def test_get_sun_hour(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_sun_hour(), 4.4)

    def test_get_sun_rise(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_sun_rise(), "06:41")

    def test_get_sun_set(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_sun_set(), "17:58")

    def test_get_cloud_cover(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_cloud_cover(), 18)

    def test_get_daylight_length(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_daylight_length(), 11.283333333333333)

    def test_get_solar_energy(self):
        weather_data = WeatherData(date.fromisoformat("2021-09-01"), Postcode("3168"), 6, 1)
        self.assertEqual(weather_data.get_solar_energy(), 3.1976366322008865)