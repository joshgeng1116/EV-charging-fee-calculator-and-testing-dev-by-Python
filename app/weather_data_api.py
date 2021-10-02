from datetime import date

import requests
from app.postcode import Postcode
from app.time_converter import time_to_minutes


class WeatherData:
    def __init__(self, check_date: date, postcode: Postcode, hour: int, duration: float) -> None:
        self.check_date = check_date
        self.postcode = postcode
        self.hour = hour
        self.duration = duration

    def get_location_id(self):
        post = str(self.postcode.get_postcode())
        url = "http://118.138.246.158/api/v1/location?postcode=" + post
        response = requests.get(url).json()
        id = response[0]['id']
        return id

    def get_weather_data_by_id(self):
        id = self.get_location_id()
        url = "http://118.138.246.158/api/v1/weather?location=" + id + "&date=" + self.check_date.isoformat()
        response = requests.get(url).json()
        si = response['sunHours']
        sr = response['sunrise'][0:5]
        ss = response['sunset'][0:5]
        hourly = response['hourlyWeatherHistory']
        for h in hourly:
            if int(h['hour']) == self.hour:
                cc = int(h['cloudCoverPct'])
        dl = (time_to_minutes(ss) - time_to_minutes(sr))/60
        return si, sr, ss, cc, dl

    def get_solar_energy(self) -> float:
        si = self.get_weather_data_by_id()[0]
        sr = self.get_weather_data_by_id()[1]
        ss = self.get_weather_data_by_id()[2]
        cc = self.get_weather_data_by_id()[3]
        dl = self.get_weather_data_by_id()[4]
        hour = self.hour
        du = self.duration
        energy: float
        if hour < int(sr[0:2]):
            energy = 0
            return energy
        elif int(sr[0:2]) <= hour <= int(ss[0:2]):
            energy = si * du / dl * (1 - cc / 100) * 50 * 0.2
            return energy
        else:
            energy = 0
            return energy

    def get_sun_hour(self):
        return self.get_weather_data_by_id()[0]

    def get_sun_rise(self):
        return self.get_weather_data_by_id()[1]

    def get_sun_set(self):
        return self.get_weather_data_by_id()[2]

    def get_cloud_cover(self):
        return self.get_weather_data_by_id()[3]

    def get_daylight_length(self):
        return self.get_weather_data_by_id()[4]

