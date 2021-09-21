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
        calc = Calculator(20, 75, 80, 22, "12:00", "2021-08-20")
        self.assertAlmostEqual(calc.time_calculation(), 2)
        self.assertEqual(calc.get_duration_in_minutes(), 120)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 120)
        # self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        # self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        # self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        # self.assertAlmostEqual(calc.cost_calculation(True, False), 6.60, places=2)
    
    # Test off-peak non-holiday (T404)
    def test_weekday_night(self):
        calc = Calculator(20, 75, 80, 22, "18:00", "2021-08-20")
        self.assertEqual(calc.time_calculation(), 2)
        self.assertEqual(calc.get_duration_in_minutes(), 120)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 120)
        # self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        # self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        # self.assertAlmostEqual(calc.cost_calculation(False, False), 3.30, places=2)
    
    # Test peak holiday(T505)
    def test_peak_holiday(self):
        calc = Calculator(20, 75, 80, 22, "12:00", "2021-08-21")
        self.assertEqual(calc.time_calculation(), 2)
        self.assertEqual(calc.get_duration_in_minutes(), 120)
        # self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        # self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        # self.assertEqual(calc.get_minutes_in_peak_holiday(), 120)
        # self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)

        # self.assertAlmostEqual(calc.cost_calculation(True, True), 7.26, places=2)

    # Test off-peak holiday (T705)

    def test_off_peak_holiday(self):
        calc = Calculator(50, 60, 50, 2, "20:00", "2021-08-22")
        self.assertAlmostEqual(calc.time_calculation(), 2.5)
        self.assertEqual(calc.get_duration_in_minutes(), 150)
        # self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        # self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        # self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        # self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 150)
        # self.assertAlmostEqual(calc.cost_calculation(False, True), 0.13, places=2)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)