"""
FIT2107 2021 Semester 2 - NullPointerException

Date Created: 2021-09-10 (Jeremy)
Date Modified: 2021-00-10

A test class to test REQ-1. 
"""
from app.calculator import *
import unittest

class TestDateTime(unittest.TestCase):

    # Test Weekday daytime (T000)
    def test_working(self):
        Calculator()
        self.assertEqual()
    
    # Test Weekday nighttime (T404)
    def test_weekday_night(self):
        calc = Calculator()
        self.assertEqual("2 Hours 0 Minute", calc.time_calculation(20, 75, 80, False, False))
        self.assertEqual("$ 3.30", calc.cost_calculation(20, 75, 80, False, False))

    # Test Weekday day and night (T603)

    # Test Weekday night and day (T702)

    # Test Weekend/Holiday daytime (T505)

    # Test Weekend/Holiday nighttime (T705)

    # Test Weekend/Holiday day and night

    # Test Weekend/Holiday night start and day stop

    