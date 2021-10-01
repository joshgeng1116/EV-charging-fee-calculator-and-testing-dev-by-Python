from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch
from app.calculator import Calculator
from app.calculator_presentation import CalculatorPresentation
from app.postcode import Postcode

class TestCalculatorPresentation(TestCase):
    
    def testHoursTime(self):
        # mock.get_duration_in_minutes.return_value = 55
        presentation = CalculatorPresentation("20", "75", "80", "5", "2021-08-20" , "12:56", "3800", Calculator)
        self.assertEqual(presentation.get_time(), "2 Hours")
        self.assertEqual(presentation.get_cost(), "$6.60")

    # T609
    def testMinutesTime(self):
        presentation = CalculatorPresentation("20", "75", "80", "7", "2021-08-20", "12:00", "3800", Calculator)
        self.assertEqual(presentation.get_cost(), "$13.20")
        self.assertEqual(presentation.get_time(), "30 Minutes")
    
    # T607
    def testHoursAndMinutesTime(self):
        presentation = CalculatorPresentation("20", "75", "80", "6", "2021-08-20", "12:00", "3800", Calculator)
        self.assertEqual(presentation.get_cost(), "$8.80")
        self.assertEqual(presentation.get_time(), "1 Hours and 14 Minutes")


        

