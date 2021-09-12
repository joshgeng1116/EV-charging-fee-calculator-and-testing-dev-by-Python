"""
FIT2107 2021 Semester 2 - NullPointerException

Date Created: 2021-09-10 (Jeremy)
Date Modified: 2021-00-10

A test class to test REQ-1. 
"""
from app.calculator import *
import unittest

class TestDateTime(unittest.TestCase):
    # Test peak non-holiday (T000)
    def test_peak_non_holiday(self):
        calc = Calculator()
        self.assertEqual(calc.time_calculation(20, 75, 80, 22), 2)
        self.assertAlmostEqual(calc.cost_calculation(20,75,80,True, False), 6.60)
    
    # Test off-peak non-holiday (T404)

    # Test peak holiday(T505)

    # Test off-peak holiday (T705)
