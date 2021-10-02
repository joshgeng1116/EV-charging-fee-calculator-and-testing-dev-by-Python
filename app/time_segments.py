from .postcode import Postcode
from .time_converter import time_to_minutes
from datetime import date, timedelta
from holidays import Australia as AUHolidays

class TimeSegments:
    def __init__(self, start_time: str, start_date: date, duration: int, postcode: Postcode) -> None:
        self.start_time = start_time
        self.start_date = start_date
        self.duration = duration
        self.postcode = postcode
        self.calculate_time_in_segment()

    def is_holiday(self, date) -> bool:
        holidays_cal = AUHolidays(prov = self.postcode.get_state())
        # If day is on the weekend 
        if (date.isoweekday() in [6, 7]):
            return True
        elif date in holidays_cal:
            return True
        else:
            return False
    
    def calculate_time_in_segment(self):
        start_time = time_to_minutes(self.start_time)
        duration = self.duration
        days = int(self.number_of_days())

        weekday_peak = 0
        weekday_off_peak = 0 
        holiday_peak = 0 
        holiday_off_peak = 0 

        # Loop through however many days there are 
        for i in range(days + 1):
            new_date: date = self.start_date + timedelta(days = i)
            peak = 0 
            off_peak = 0
            if (i == 0):
                if (days == 0):
                    new_duration = duration
                    off_peak, peak, remain_duration = self.__minutes_off_peak_and_peak(start_time, int(new_duration))
                else:
                    new_duration = 1440 - start_time
                    off_peak, peak, remain_duration = self.__minutes_off_peak_and_peak(start_time, int(new_duration))
                    duration -= remain_duration
            elif (0 < i and i < days):
                new_duration = 1440
                # off_peak, peak, remain_duration = self.__minutes_off_peak_and_peak(0, int(new_duration))
                off_peak = 720
                peak = 720
                duration -= 1440
            elif (i != 0 and i == days):
                new_duration = duration
                off_peak, peak, remain_duration = self.__minutes_off_peak_and_peak(0, int(new_duration))
            
            if self.is_holiday(new_date) == True:
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
            elif (start_time_mins + duration_mins >= 1080 and start_time_mins + duration_mins <= 1440):
                peak += 1080 - start_time_mins
                off_peak += start_time_mins + duration_mins - 1080
        elif (start_time_mins >= 1080 and start_time_mins + duration_mins <= 1440):
            off_peak = duration_mins
        duration = peak + off_peak
        return (off_peak, peak, duration)
    
    def number_of_days(self) -> int:
        start_time_minutes = time_to_minutes(self.start_time)
        time_cost_in_minutes = self.duration
        days = (start_time_minutes + time_cost_in_minutes) // 1440
        return days


    def get_minutes_in_peak_weekday(self):
        return self.calculate_time_in_segment()[1]

    def get_minutes_in_offpeak_weekday(self):
        return self.calculate_time_in_segment()[0]
    
    def get_minutes_in_peak_holiday(self):
        return self.calculate_time_in_segment()[3]
    
    def get_minutes_in_offpeak_holiday(self):
        return self.calculate_time_in_segment()[2]


    
        