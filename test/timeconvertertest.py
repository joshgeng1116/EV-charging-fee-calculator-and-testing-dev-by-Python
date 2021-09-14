

import unittest
from app.time_converter import time_to_minutes

class TimeCoverterTest(unittest.TestCase):

    # Test when the time input is 23:59
    def test_time1(self):
        time_to_minutes('23.59')

    # Test when the time input is 00:00
    def test_time2(self):
        time_to_minutes('00:00')

    # Test when the time input is 12:00
    def test_time3(self):
        time_to_minutes('12:00')

    # Test when the time input is 15:07
    def test_time4(self):
        time_to_minutes('15:07')
