from unittest import TestCase
from app.time_segments import TimeSegments
from datetime import date
from app.postcode import Postcode
class TestTimeSegment(TestCase):
    def test_is_holiday(self):
        # Test Weekday 
        segments = TimeSegments("12:00", date.fromisoformat("2021-09-27"), 120, Postcode("3800"))
        self.assertFalse(segments.is_holiday(segments.start_date))
        
        # Test Saturday
        segments = TimeSegments("12:00", date.fromisoformat("2021-09-25"), 120, Postcode("3800"))
        self.assertTrue(segments.is_holiday(segments.start_date))
        
        # Test Sunday
        segments = TimeSegments("12:00", date.fromisoformat("2021-09-26"), 120, Postcode("3800"))
        self.assertTrue(segments.is_holiday(segments.start_date))
        
        # Test Grandfinal day
        segments = TimeSegments("12:00", date.fromisoformat("2021-09-24"), 120, Postcode("3800"))
        self.assertTrue(segments.is_holiday(segments.start_date))

        # Test anzac day in NSW
        segments = TimeSegments("12:00", date.fromisoformat("2021-09-25"), 120, Postcode("2000"))
        self.assertTrue(segments.is_holiday(segments.start_date))

    def test_peak_time(self):
        segments = TimeSegments("12:00", date.fromisoformat("2021-08-20"), 120, Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 120)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 0)
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 0)
    
    def test_morning_combo(self):
        segments = TimeSegments("05:00", date.fromisoformat("2021-08-20"), 120, Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 60)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 60)
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 0)
    
    def test_weekday_weekend_offpeak(self):
        segments = TimeSegments("23:00", date.fromisoformat("2021-08-20"), 120, Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 60) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 60)

    def test_weekend_weekday_offpeak(self):
        segments = TimeSegments("23:00", date.fromisoformat("2021-08-22"), 120, Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 60) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 60)
    
    def test_holiday_weekday_offpeak(self):
        segments = TimeSegments("23:00", date.fromisoformat("2021-09-24"), 120 ,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 0) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 120)

    def test_evening_combo(self):
        segments = TimeSegments("17:00", date.fromisoformat("2021-08-20"), 120 ,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 60)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 60) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 0)
    
    def test_long_time_combo_weekday(self):
        segments = TimeSegments("17:00", date.fromisoformat("2021-08-18"), 1440,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 720)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 720) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 0)

    def test_long_time_combo_weekend(self):
        segments = TimeSegments("17:00", date.fromisoformat("2021-08-21"), 1560 ,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 0) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 780)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 780)
        
    def test_long_time_combo_weekday_weekend(self):
        segments = TimeSegments("17:00", date.fromisoformat("2021-08-20"), 1560 ,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 60)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 360) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 720)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 420)

    def test_long_time_combo_weekend_weekday(self):
        segments = TimeSegments("17:00", date.fromisoformat("2021-08-22"), 1560 ,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 720)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 420) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 60)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 360)

    def test_two_days_combo(self):
        segments = TimeSegments("17:00", date.fromisoformat("2021-08-16"), 2880 ,Postcode("3800"))
        self.assertEqual(segments.get_minutes_in_peak_weekday(), 1440)
        self.assertEqual(segments.get_minutes_in_offpeak_weekday(), 1440) 
        self.assertEqual(segments.get_minutes_in_peak_holiday(), 0)
        self.assertEqual(segments.get_minutes_in_offpeak_holiday(), 0)