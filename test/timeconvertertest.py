from datetime import time
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
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            time_to_minutes("abc")
    
    def test_string_in_correct_format(self):
        with self.assertRaises(ValueError):
            time_to_minutes("abc:abc")
    
    def test_lowwer_boundary(self):
        # Test Both minutes and hours out of range 
        with self.assertRaises(ValueError):
            time_to_minutes("-01:-01")
        # Test Hours out of range 
        with self.assertRaises(ValueError):
            time_to_minutes("-01:00")
        # Test minutes out of range 
        with self.assertRaises(ValueError):
            time_to_minutes("00:-01")
        # Test first working value 
        self.assertEqual(time_to_minutes("00:00"), 0)

    def test_upper_boundary(self):
        # Test both minutes and hour out of range 
        with self.assertRaises(ValueError):
            time_to_minutes("24:01")
        # Test hours above range 
        with self.assertRaises(ValueError):
            time_to_minutes("24:00")
        # Test minutes above range
        with self.assertRaises(ValueError):
            time_to_minutes("23:60")
        # Test last working value 
        self.assertEqual(time_to_minutes("23:59"), 1439)