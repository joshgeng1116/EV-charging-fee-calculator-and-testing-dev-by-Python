"""
FIT2107 2021 Semester 2 - NullPointerException

Date Created: 2021-09-10 (Jeremy)
Date Modified: 2021-00-10

A test class to test REQ-1. 
"""

from app.calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    # Test peak non-holiday (T000)
    def test_peak_non_holiday(self):
        calc = Calculator(20, 75, 80, 22)
        self.assertEqual(calc.time_calculation(), 120)
        # self.assertAlmostEqual(calc.cost_calculation(True, False), 6.60, places=2)
    
    # Test off-peak non-holiday (T404)
    def test_weekday_night(self):
        calc = Calculator(20, 75, 80, 22)
        self.assertEqual(calc.time_calculation(), 120)
        # self.assertAlmostEqual(calc.cost_calculation(False, False), 3.30, places=2)
    # Test peak holiday(T505)
    def test_peak_holiday(self):
        calc = Calculator(20, 75, 80, 22)
        self.assertEqual(calc.time_calculation(), 120)
        # self.assertAlmostEqual(calc.cost_calculation(True, True), 7.26, places=2)

    # Test off-peak holiday (T705)
    def test_off_peak_holiday(self):
        calc = Calculator(50, 60, 50, 2)
        self.assertAlmostEqual(calc.time_calculation(), 150)
        # self.assertAlmostEqual(calc.cost_calculation(False, True), 0.13, places=2)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)