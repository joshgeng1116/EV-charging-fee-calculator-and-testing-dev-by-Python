from app.time_segments import TimeSegments
from app.postcode import Postcode
from app.time_converter import time_to_minutes
from datetime import date, timedelta
from holidays import Australia as AUHolidays
from app.weather_data_api import WeatherData
from app.chargeconfig import ChargingConfig


class EnergyCostCalculator(TimeSegments):
    def __init__(self, start_time: str, start_date: date, duration: float, postcode: Postcode,
                 config: ChargingConfig) -> None:
        TimeSegments.__init__(self, start_time, start_date, duration, postcode)
        self.config = config

    def calculate_cost(self):
        start_time = self.start_time
        remain_duration = self.duration
        days = int(self.number_of_days())
        cost: float = 0
        for i in range(days + 1):
            new_date: date = self.start_date + timedelta(days=i)
            if i == 0:
                hour = int(start_time[0:2])
                while hour < 24 and remain_duration > 60:
                    if hour == int(start_time[0:2]):
                        du = (60 - int(start_time[3:])) / 60
                        cost += self.hourly_cost_cal(new_date, hour, du)
                    else:
                        du = 1
                        cost += self.hourly_cost_cal(new_date, hour, du)
                    hour += 1
                    remain_duration -= du * 60
                if hour < 24 and remain_duration < 60:
                    if hour == int(start_time[0:2]):
                        du = (60 - int(start_time[3:]) - remain_duration) / 60
                        cost += self.hourly_cost_cal(new_date, hour, du)

                    else:
                        du = remain_duration / 60
                        cost += self.hourly_cost_cal(new_date, hour, du)

            elif 0 < i <= days:
                hour = 0
                start_time = "00:00"
                while hour < 24 and remain_duration > 60:
                    du = 1
                    cost += self.hourly_cost_cal(new_date, hour, du)
                    hour += 1
                    remain_duration -= du * 60
                if hour < 24 and remain_duration < 60:
                    du = remain_duration / 60
                    cost += self.hourly_cost_cal(new_date, hour, du)

        return cost

    def is_peak(self, hour) -> bool:
        if 6 <= hour <= 18:
            return True
        else:
            return False

    def hourly_cost_cal(self, new_date, hour, du) -> float:
        energy: float
        if self.is_peak(hour):
            if self.is_holiday(new_date):
                weather_data = WeatherData(new_date, self.postcode, hour, du)
                energy = self.config.get_power() * du - weather_data.get_solar_energy()
                cost = energy * self.config.get_base_price()/100 * 1.1
                return cost
            else:
                weather_data = WeatherData(new_date, self.postcode, hour, du)
                energy = self.config.get_power() * du - weather_data.get_solar_energy()
                cost = energy * self.config.get_base_price()/100
                return cost
        else:
            if self.is_holiday(new_date):
                weather_data = WeatherData(new_date, self.postcode, hour, du)
                energy = self.config.get_power() * du - weather_data.get_solar_energy()
                cost = energy * self.config.get_base_price()/100 * 1.1 * 0.5
                return cost
            else:
                weather_data = WeatherData(new_date, self.postcode, hour, du)
                energy = self.config.get_power() * du - weather_data.get_solar_energy()
                cost = energy * self.config.get_base_price()/100 * 0.5
                return cost
