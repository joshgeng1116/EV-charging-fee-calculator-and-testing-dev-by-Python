"""
FIT2107 2021 Semester 2 - NullPointerException

Date First Modified: 2021-09-10
Date Modified: 2021-00-10

A file which a class called calculator that runs the calculations for the 
Joules Up battery charging online calculator. 
"""
from math import ceil

from app.energy_cal import EnergyCostCalculator
from app.chargeconfig import ChargingConfig
from app.time_segments import TimeSegments
from .postcode import Postcode
import math
import datetime
from datetime import date, timedelta, time

from .time_converter import *
from app import time_converter


class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self, inital_state: float, final_state: float, capacity: float,
                 config: ChargingConfig, start_time: time, start_date: date, postcode: Postcode):
        self.initial_state = inital_state
        self.final_state = final_state
        self.capacity = capacity
        self.config = config
        self.start_time = start_time
        self.start_date = start_date
        self.postcode = postcode
        self.timeSegments = TimeSegments(start_time, date.fromisoformat(self.start_date),
                                         self.get_duration_in_minutes(), self.postcode)

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self) -> float:
        peek_weekday = self.get_minutes_in_peak_weekday() / self.get_duration_in_minutes()
        peek_holiday = self.get_minutes_in_peak_holiday() / self.get_duration_in_minutes()
        offpeak_weekday = self.get_minutes_in_offpeak_weekday() / self.get_duration_in_minutes()
        offpeak_holiday = self.get_minutes_in_offpeak_holiday() / self.get_duration_in_minutes()

        cost = ((self.final_state - self.initial_state) / 100) * self.capacity * (self.config.get_base_price() / 100)
        cost_with_time_consideration = peek_weekday * cost + offpeak_weekday * 0.5 * cost + peek_holiday * 1.1 * cost
        cost_with_time_consideration += offpeak_holiday * cost * 0.5 * 1.1
        return cost_with_time_consideration

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self) -> float:
        """
        A method which returns the time a charge will take in hours. 
        """
        time = (self.final_state - self.initial_state) / 100 * self.capacity / self.config.get_power()
        return time

    def get_duration_in_minutes(self) -> float:
        return math.ceil(self.time_calculation() * 60)

    def get_minutes_in_peak_weekday(self):
        return self.timeSegments.get_minutes_in_peak_weekday()

    def get_minutes_in_offpeak_weekday(self):
        return self.timeSegments.get_minutes_in_offpeak_weekday()

    def get_minutes_in_peak_holiday(self):
        return self.timeSegments.get_minutes_in_peak_holiday()

    def get_minutes_in_offpeak_holiday(self):
        return self.timeSegments.get_minutes_in_offpeak_holiday()



class CalculatorWithSolarEnergy(Calculator):
    def cost_calculation(self) -> float:
        current_date: date = datetime.date.today()
        check_date: date = current_date - timedelta(days=2)
        start_date: date = self.date_converter(self.start_date)
        total_cost = 0
        if start_date > check_date:
            for i in range(3):
                new_date = start_date.replace(year=int(start_date.year) - (i + 1))
                total_cost += EnergyCostCalculator(self.start_time, new_date, self.get_duration_in_minutes(),
                                                   self.postcode, self.config).calculate_cost()
        else:
            for i in range(3):
                new_date = start_date.replace(year=int(start_date.year) - i)
                total_cost += EnergyCostCalculator(self.start_time, new_date, self.get_duration_in_minutes(),
                                                   self.postcode, self.config).calculate_cost()
        average_cost = total_cost / 3
        return average_cost

    def date_converter(self, start_date: str) -> date:
        new_date = date.fromisoformat(start_date)
        if new_date.month == 2 and new_date.day == 29:
            new_date = new_date.replace(day=28)
            if new_date.year > datetime.date.today().year:
                new_date = new_date.replace(year=datetime.date.today().year)
                return new_date
            else:
                return new_date
        else:
            if new_date.year > datetime.date.today().year:
                new_date = new_date.replace(year=datetime.date.today().year)
                return new_date
            else:
                return new_date
