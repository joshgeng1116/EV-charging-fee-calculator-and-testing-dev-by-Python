from unittest import TestCase
from app.time_segments import TimeSegments
from datetime import date
from app.postcode import Postcode
class TestTimeSegment(TestCase):
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