

import unittest
from app.time_converter import time_to_minutes

class TimeCoverterTest(unittest.TestCase):

    # Test when the time input is 23:59
    def test_time1(self):
        self.assertEqual(time_to_minutes('23:59'), 1439)

    # Test when the time input is 00:00
    def test_time2(self):
        self.assertEqual(time_to_minutes('00:00'), 0)

    # Test when the time input is 12:00
    def test_time3(self):
        self.assertEqual(time_to_minutes('12:00'), 720)

    # Test when the time input is 15:07
    def test_time4(self):
        self.assertEqual(time_to_minutes('15:07'), 907)
