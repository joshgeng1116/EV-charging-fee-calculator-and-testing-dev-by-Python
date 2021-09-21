from app.postcode import Postcode
import unittest

class PostcodeTest(unittest.TestCase):
    def test_postcode_state_nsw(self):
        self.assertEquals(Postcode("1000").get_state(), "NSW", msg = "Postcode 1000 should be in NSW")
        self.assertEquals(Postcode("1500").get_state(), "NSW", msg = "Postcode 1500 should be in NSW")
        self.assertEquals(Postcode("1999").get_state(), "NSW", msg = "Postcode 1999 should be in NSW")
        self.assertEquals(Postcode("2000").get_state(), "NSW", msg = "Postcode 2000 should be in NSW")
        self.assertEquals(Postcode("2100").get_state(), "NSW", msg = "Postcode 2100 should be in NSW")
        self.assertEquals(Postcode("2599").get_state(), "NSW", msg = "Postcode 2599 should be in NSW")
        self.assertEquals(Postcode("2619").get_state(), "NSW", msg = "Postcode 2619 should be in NSW")
        self.assertEquals(Postcode("2700").get_state(), "NSW", msg = "Postcode 2700 should be in NSW")
        self.assertEquals(Postcode("2899").get_state(), "NSW", msg = "Postcode 2899 should be in NSW")
        self.assertEquals(Postcode("2921").get_state(), "NSW", msg = "Postcode 2921 should be in NSW")
        self.assertEquals(Postcode("2950").get_state(), "NSW", msg = "Postcode 2950 should be in NSW")
        self.assertEquals(Postcode("2999").get_state(), "NSW", msg = "Postcode 2999 should be in NSW")
    
    def test_postcode_state_act(self):
        self.assertEquals(Postcode("0200").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("0250").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("0299").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("2600").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("2610").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("2618").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("2900").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("2910").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEquals(Postcode("2920").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
