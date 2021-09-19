"""
FIT2107 2021 Semester 2 - NullPointerException

Date First Modified: 2021-09-10
Date Modified: 2021-00-10

A file which a class called calculator that runs the calculations for the 
Joules Up battery charging online calculator. 
"""

from datetime import date, timedelta, time

from .time_converter import *
from app import time_converter


class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self, inital_state, final_state, capacity, power, start_time, start_date):
        self.initial_state = inital_state
        self.final_state = final_state 
        self.capacity = capacity
        self.power = power
        self.start_time = start_time
        self.start_date = start_date
        

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, is_peak, is_holiday):
        if is_peak:
            base_price = 100
        else:
            base_price = 50

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (self.final_state - self.initial_state) / 100 * self.capacity * self.base_price / 100 * surcharge_factor
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self) -> float:
        """
        A method which returns the time a charge will take in hours. 
        """
        time = (self.final_state - self.initial_state) / 100 * self.capacity / self.power
        return time


    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date):
        return False

    def is_peak(self):
        pass

    def calculate_time_in_segment(self):
        start_time = time_to_minutes(self.start_time)
        duration = self.get_duration_in_minutes()
        days = self.number_of_days()

        weekday_peak = 0
        weekday_off_peak = 0 

        # Loop through however many days there are 
        for i in range(days + 1):
            new_date: str = )date.fromisoformat(self.start_date) + timedelta(days = i)).isoformat()
            if is_holiday(self.start_date) == False:
                if (start_time < 360):
                    if (start_time + duration < 360):
                        weekday_off_peak += duration
                    elif (start_time + duration >= 360 and start_time + duration < 1080):
                        weekday_peak += start_time + duration - 360
                        weekday_off_peak += 360 - start_time
                    elif (start_time + duration >= 1080 and start_time + duration < 1440):
                        weekday_peak += 720
                        weekday_off_peak += duration - 720
                elif (start_time >= 360 and start_time < 1080):
                    if (start_time + duration >= 360 and start_time + duration < 1080):
                        weekday_peak += duration
                    elif (start_time + duration >= 1080 and start_time + duration < 1440):
                        weekday_peak += 1080 - start_time
                        weekday_off_peak += start_time + duration - 1080
                elif (start_time >= 1080 and start_time + duration < 1440):
                    weekday_off_peak = duration




                    




    def get_duration_in_minutes(self) -> float:
        return self.time_calculation() * 60

    # to be acquired through API
    def get_sun_hour(self, sun_hour):
        pass

    # to be acquired through API
    def get_solar_energy_duration(self, start_time):
        pass

    # to be acquired through API
    def get_day_light_length(self, start_time):
        pass

    # to be acquired through API
    def get_solar_insolation(self, solar_insolation):
        pass

    # to be acquired through API
    def get_cloud_cover(self):
        pass

    def calculate_solar_energy(self):
        pass

    def number_of_days(self) ->float:
        start_time_minutes = time_to_minutes(self.start_time)
        time_cost_in_minutes = self.get_duration_in_minutes()
        days = (start_time_minutes + time_cost_in_minutes) // 1440
        return days

