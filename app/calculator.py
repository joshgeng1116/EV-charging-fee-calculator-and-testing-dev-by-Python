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
    def is_holiday(self, start_date: date, state: str) -> bool:
        return False

    def is_peak(self):
        pass

    def __calculate_time_in_segment(self):
        start_time = time_to_minutes(self.start_time)
        duration = self.get_duration_in_minutes()
        days = int(self.number_of_days())

        weekday_peak = 0
        weekday_off_peak = 0 
        holiday_peak = 0 
        holiday_off_peak = 0 

        # Loop through however many days there are 
        for i in range(days + 1):
            new_date: str = (date.fromisoformat(self.start_date) + timedelta(days = i))
            peak = 0 
            off_peak = 0
            if (i == 0):
                if (days == 0):
                    new_duration = duration
                else:
                    new_duration = start_time + duration - 1400 * days
                off_peak, peak, new_duration = self.__minutes_off_peak_and_peak(start_time, int(new_duration))
                print(days)
                duration -= new_duration
            elif (0 < i and i < days):
                new_duration = 1440
                off_peak, peak, remain_duration = self.__minutes_off_peak_and_peak(0, int(new_duration))
                duration -= 1440
            elif (i != 0 and i == days):
                new_duration = duration
                off_peak, peak, new_duration = self.__minutes_off_peak_and_peak(0, int(new_duration))
            
            if self.is_holiday(new_date, "VIC") == True:
                holiday_off_peak += off_peak
                holiday_peak += peak
            else:
                weekday_off_peak += off_peak
                weekday_peak += peak
        
        return (weekday_off_peak, weekday_peak, holiday_off_peak, holiday_peak)

    def __minutes_off_peak_and_peak(self, start_time_mins: int, duration_mins: int):
        peak = 0
        off_peak = 0
        if (start_time_mins < 360):
            if (start_time_mins + duration_mins < 360):
                off_peak += duration_mins
            elif (start_time_mins + duration_mins >= 360 and start_time_mins + duration_mins < 1080):
                peak += start_time_mins + duration_mins - 360
                off_peak += 360 - start_time_mins
            elif (start_time_mins + duration_mins >= 1080 and start_time_mins + duration_mins < 1440):
                peak += 720
                off_peak += duration_mins - 720
        elif (start_time_mins >= 360 and start_time_mins < 1080):
            if (start_time_mins + duration_mins >= 360 and start_time_mins + duration_mins < 1080):
                peak += duration_mins
            elif (start_time_mins + duration_mins >= 1080 and start_time_mins + duration_mins < 1440):
                peak += 1080 - start_time_mins
                off_peak += start_time_mins + duration_mins - 1080
        elif (start_time_mins >= 1080 and start_time_mins + duration_mins < 1440):
            off_peak = duration_mins
        duration = peak + off_peak
        return (off_peak, peak, duration)

    def get_minutes_in_peak_weekday(self):
        return self.__calculate_time_in_segment()[1]

    def get_minutes_in_offpeak_weekday(self):
        return self.__calculate_time_in_segment()[0]
    
    def get_minutes_in_peak_holiday(self):
        return self.__calculate_time_in_segment()[3]
    
    def get_minutes_in_offpeak_holiday(self):
        return self.__calculate_time_in_segment()[2]

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

    def number_of_days(self) ->int:
        start_time_minutes = time_to_minutes(self.start_time)
        time_cost_in_minutes = self.get_duration_in_minutes()
        days = (start_time_minutes + time_cost_in_minutes) // 1440
        return days

