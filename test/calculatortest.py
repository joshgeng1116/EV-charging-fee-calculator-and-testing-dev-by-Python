"""
FIT2107 2021 Semester 2 - NullPointerException

Date Created: 2021-09-10 (Jeremy)
Date Modified: 2021-00-10

A test class to test REQ-1. 
"""

from app.postcode import Postcode
from app.calculator import Calculator
from app.chargeconfig import JoulesupChargeConfigurations
import unittest


class CalculatorTest(unittest.TestCase):
    # Test peak non-holiday (T000)
    def test_peak_non_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_5, "12:00", "2021-08-20", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 2)
        self.assertEqual(calc.get_duration_in_minutes(), 120)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 120)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 6.60, places=2)

    # Test off-peak non-holiday (T404)
    def test_weekday_night(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_5, "18:00", "2021-08-20", Postcode("3800"))
        self.assertEqual(calc.time_calculation(), 2)
        self.assertEqual(calc.get_duration_in_minutes(), 120)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 120)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 3.30, places=2)

    # Test peak holiday(T505)
    def test_peak_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_5, "12:00", "2021-08-21", Postcode("3800"))
        self.assertEqual(calc.time_calculation(), 2)
        self.assertEqual(calc.get_duration_in_minutes(), 120)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 120)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 7.26, places=2)

    # Test off-peak holiday (T705)
    def test_off_peak_holiday(self):
        calc = Calculator(50, 60, 50, JoulesupChargeConfigurations.LEVEL_1, "20:00", "2021-08-22", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 2.5)
        self.assertEqual(calc.get_duration_in_minutes(), 150)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 150)
        self.assertAlmostEqual(calc.cost_calculation(), 0.14, places=2)

    # Test charging config 2, peak to off-peak non-holiday (T604)
    def test_config_two(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_2, "12:00", "2021-08-19", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 12.22, places=2)
        self.assertEqual(calc.get_duration_in_minutes(), 734)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 360)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 374)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 2.46, places=2)

    # Test peak to off-peak holiday (NEW)
    def test_peak_off_peak_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_2, "11:00", "2021-08-22", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 12.22, places=2)
        self.assertEqual(calc.get_duration_in_minutes(), 734)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 420)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 314)
        self.assertAlmostEqual(calc.cost_calculation(), 2.85, places=2)

    # Test off-peak to peak non-holiday (NEW)
    def test_off_peak_peak_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_2, "00:00", "2021-08-19", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 12.22, places=2)
        self.assertEqual(calc.get_duration_in_minutes(), 734)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 374)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 360)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 2.49, places=2)

    # Test off-peak to peak non-holiday (NEW)
    def test_off_peak_peak_non_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_2, "00:00", "2021-08-19", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 12.22, places=2)
        self.assertEqual(calc.get_duration_in_minutes(), 734)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 374)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 360)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 2.49, places=2)

    # Test off-peak to peak holiday (NEW)
    def test_off_peak_peak_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_2, "00:00", "2021-08-21", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 12.22, places=2)
        self.assertEqual(calc.get_duration_in_minutes(), 734)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 374)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 360)
        self.assertAlmostEqual(calc.cost_calculation(), 2.74, places=2)

    # Test peek to non-peek to peek charging in weekday/Charge config 1 (T603)
    def test_config_one(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_1, "12:00", "2021-08-19", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 22)
        self.assertEqual(calc.get_duration_in_minutes(), 1320)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 600)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 720)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 1.60, places=2)

    # Test peek to non-peek to peek charging in holiday(NEW)
    def test_peek_non_peek_peek_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_1, "12:00", "2021-08-21", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 22)
        self.assertEqual(calc.get_duration_in_minutes(), 1320)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 600)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 720)
        self.assertAlmostEqual(calc.cost_calculation(), 1.76, places=2)

    # Test non-peek to peek to non-peek charging in weekday(NEW)
    def test_non_peak_peak_non_peak_weekday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_1, "00:00", "2021-08-19", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 22)
        self.assertEqual(calc.get_duration_in_minutes(), 1320)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 720)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 600)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 0)
        self.assertAlmostEqual(calc.cost_calculation(), 1.70, places=2)

    # Test non-peek to peek to non-peek charging in holiday(NEW)
    def test_non_peak_peak_non_peak_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_1, "00:00", "2021-08-21", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 22)
        self.assertEqual(calc.get_duration_in_minutes(), 1320)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 720)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 600)
        self.assertAlmostEqual(calc.cost_calculation(), 1.87, places=2)

    # Test peek to non-peek to peek charging cross weekday to holiday(NEW)
    def test_peak_non_peak_peak_weekday_holiday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_1, "16:00", "2021-08-20", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 22)
        self.assertEqual(calc.get_duration_in_minutes(), 1320)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 120)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 360)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 480)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 360)
        self.assertAlmostEqual(calc.cost_calculation(), 1.71, places=2)

    # Test peek to non-peek to peek charging cross holiday to weekday(NEW)
    def test_peak_non_peak_peak_holiday_weekday(self):
        calc = Calculator(20, 75, 80, JoulesupChargeConfigurations.LEVEL_1, "16:00", "2021-08-22", Postcode("3800"))
        self.assertAlmostEqual(calc.time_calculation(), 22)
        self.assertEqual(calc.get_duration_in_minutes(), 1320)
        self.assertEqual(calc.get_minutes_in_peak_weekday(), 480)
        self.assertEqual(calc.get_minutes_in_offpeak_weekday(), 360)
        self.assertEqual(calc.get_minutes_in_peak_holiday(), 120)
        self.assertEqual(calc.get_minutes_in_offpeak_holiday(), 360)
        self.assertAlmostEqual(calc.cost_calculation(), 1.65, places=2)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
