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

    def get_energy(self) -> float:
        post = str(self.postcode.get_postcode())
        url = "http://118.138.246.158/api/v1/location?postcode=" + post
        response = requests.get(url).json()
        id = response[0]['id']
        return self.get_hourly_data(id)

    def get_hourly_data(self, id: str):
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
        energy = self.calculate_hourly_solar_energy(si, sr, ss, dl, self.hour, cc, self.duration)
        return energy

    def calculate_hourly_solar_energy(self, si: int, sr: str, ss: str, dl: int, hour: int, cc: int, du: float) -> float:
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
