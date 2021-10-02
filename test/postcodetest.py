from app.postcode import Postcode, InvalidPostcodeException
import unittest

class PostcodeTest(unittest.TestCase):
    def test_postcode_state_nsw(self):
        self.assertEqual(Postcode("1000").get_state(), "NSW", msg = "Postcode 1000 should be in NSW")
        self.assertEqual(Postcode("1500").get_state(), "NSW", msg = "Postcode 1500 should be in NSW")
        self.assertEqual(Postcode("1999").get_state(), "NSW", msg = "Postcode 1999 should be in NSW")
        self.assertEqual(Postcode("2000").get_state(), "NSW", msg = "Postcode 2000 should be in NSW")
        self.assertEqual(Postcode("2100").get_state(), "NSW", msg = "Postcode 2100 should be in NSW")
        self.assertEqual(Postcode("2599").get_state(), "NSW", msg = "Postcode 2599 should be in NSW")
        self.assertEqual(Postcode("2619").get_state(), "NSW", msg = "Postcode 2619 should be in NSW")
        self.assertEqual(Postcode("2700").get_state(), "NSW", msg = "Postcode 2700 should be in NSW")
        self.assertEqual(Postcode("2899").get_state(), "NSW", msg = "Postcode 2899 should be in NSW")
        self.assertEqual(Postcode("2921").get_state(), "NSW", msg = "Postcode 2921 should be in NSW")
        self.assertEqual(Postcode("2950").get_state(), "NSW", msg = "Postcode 2950 should be in NSW")
        self.assertEqual(Postcode("2999").get_state(), "NSW", msg = "Postcode 2999 should be in NSW")
    
    def test_postcode_state_act(self):
        self.assertEqual(Postcode("0200").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("0250").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("0299").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("2600").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("2610").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("2618").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("2900").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("2910").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")
        self.assertEqual(Postcode("2920").get_state(), "ACT", msg = "Postcode 0200 should be in ACT")


    def test_postcode_state_vic(self):
        # Test range 3000 - 3999 including boundaries
        self.assertEqual(Postcode("3000").get_state(), "VIC", msg = "Postcode 3000 should be in VIC")
        self.assertNotEqual(Postcode("2999").get_state(), "VIC", msg = "Postcode 3000 should not be in VIC")
        self.assertEqual(Postcode("3800").get_state(), "VIC", msg = "Postcode 3800 should be in VIC")
        self.assertEqual(Postcode("3999").get_state(), "VIC", msg = "Postcode 3999 should be in VIC")
        self.assertNotEqual(Postcode("4000").get_state(), "VIC", msg = "Postcode 3999 should not be in VIC")

        # Test range 8000 - 8999
        self.assertEqual(Postcode("8000").get_state(), "VIC", msg = "Postcode 8000 should be in VIC")
        self.assertNotEqual(Postcode("7999").get_state(), "VIC", msg = "Postcode 8000 should not be in VIC")
        self.assertEqual(Postcode("8800").get_state(), "VIC", msg = "Postcode 8800 should be in VIC")
        self.assertEqual(Postcode("8999").get_state(), "VIC", msg = "Postcode 8999 should be in VIC")
        self.assertNotEqual(Postcode("9000").get_state(), "VIC", msg = "Postcode 9000 should not be in VIC")

    def test_postcode_state_qld(self):
        # 4000—4999
        self.assertEqual(Postcode("4000").get_state(), "QLD", msg = "Postcode 4000 should be in QLD")
        self.assertNotEqual(Postcode("3999").get_state(), "QLD", msg = "Postcode 3999 should not be in QLD")
        self.assertEqual(Postcode("4800").get_state(), "QLD", msg = "Postcode 4800 should be in QLD")
        self.assertEqual(Postcode("4999").get_state(), "QLD", msg = "Postcode 4999 should be in QLD")
        self.assertNotEqual(Postcode("5000").get_state(), "QLD", msg = "Postcode 4999 should not be in  QLD")
        
        # 9000—9999 (LVRs and PO Boxes only)
        self.assertEqual(Postcode("9000").get_state(), "QLD", msg = "Postcode 9000 should be in QLD")
        self.assertNotEqual(Postcode("8999").get_state(), "QLD", msg = "Postcode 8999 should not be in QLD")
        self.assertEqual(Postcode("9800").get_state(), "QLD", msg = "Postcode 9800 should be in QLD")
        self.assertEqual(Postcode("9999").get_state(), "QLD", msg = "Postcode 9999 should be in QLD")
    
    def test_postcode_state_sa(self):
        self.assertEqual(Postcode("5000").get_state(), "SA", msg = "Postcode 5000 should be in SA")
        self.assertNotEqual(Postcode("4999").get_state(), "SA", msg = "Postcode 4999 should not be in SA")
        self.assertEqual(Postcode("5100").get_state(), "SA", msg = "Postcode 5100 should be in SA")
        self.assertEqual(Postcode("5999").get_state(), "SA", msg = "Postcode 5100 should be in SA")
        self.assertNotEqual(Postcode("6000").get_state(), "SA", msg = "Postcode 5100 should notbe in SA")
    
    def test_postcode_state_wa(self):
        self.assertEqual(Postcode("6000").get_state(), "WA", msg = "Postcode 6000 should be in WA")
        self.assertNotEqual(Postcode("5999").get_state(), "WA", msg = "Postcode 5999 should not be in WA")
        self.assertEqual(Postcode("6100").get_state(), "WA", msg = "Postcode 6100 should be in WA")
        self.assertEqual(Postcode("6999").get_state(), "WA", msg = "Postcode 6999 should be in WA")
        self.assertNotEqual(Postcode("7000").get_state(), "WA", msg = "Postcode 7000 should notbe in WA")

    def test_postcode_state_tas(self):
        self.assertEqual(Postcode("7000").get_state(), "TAS", msg = "Postcode 7000 should be in TAS")
        self.assertNotEqual(Postcode("6999").get_state(), "TAS", msg = "Postcode 6999 should not be in TAS")
        self.assertEqual(Postcode("7100").get_state(), "TAS", msg = "Postcode 7100 should be in TAS")
        self.assertEqual(Postcode("7999").get_state(), "TAS", msg = "Postcode 7999 should be in TAS")
        self.assertNotEqual(Postcode("8000").get_state(), "TAS", msg = "Postcode 8000 should notbe in TAS")

    def test_postcode_state_nt(self):
        self.assertEqual(Postcode("0800").get_state(), "NT", msg = "Postcode 0800 should be in NT")
        with self.assertRaises(InvalidPostcodeException, msg = "Postcode 0799 should not be in NT"):
            self.assertNotEqual(Postcode("0799").get_state(), "NT", msg = "Postcode 0799 should not be in NT")
        self.assertEqual(Postcode("0810").get_state(), "NT", msg = "Postcode 0810 should be in NT")
        self.assertEqual(Postcode("0999").get_state(), "NT", msg = "Postcode 0999 should be in NT")
        self.assertNotEqual(Postcode("1000").get_state(), "NT", msg = "Postcode 1000 should notbe in NT")

    def test_get_postcode(self):
        self.assertEqual(Postcode("3000").get_postcode(), "3000", msg = "Postcode 3000 inputed into the Postcode should be 3000")    
        
        with self.assertRaises(InvalidPostcodeException, msg = "A 3 digit postcode should be invalid"):
            Postcode("800").get_postcode()
        with self.assertRaises(InvalidPostcodeException, msg = "A 5 digit postcode should be invalid"):
            Postcode("10000").get_postcode()
        