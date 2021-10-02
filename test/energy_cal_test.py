from app.postcode import Postcode
from app.time_converter import time_to_minutes
from datetime import date, timedelta
from holidays import Australia as AUHolidays
from app.weather_data_api import WeatherData
from app.chargeconfig import ChargingConfig, JoulesupChargeConfigurations
from app.energy_cal import EnergyCalculator

class

a = EnergyCalculator("12:00", date.fromisoformat("2021-9-20"), 120, Postcode("3168"), JoulesupChargeConfigurations.LEVEL_5)
cost = a.cost()