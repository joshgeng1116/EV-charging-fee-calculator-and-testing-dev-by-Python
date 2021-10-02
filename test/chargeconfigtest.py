from app.postcode import InvalidPostcodeException
from flask import config
from app.chargeconfig import ChargingConfig, InvalidConfigException, JoulesupChargeConfigurations
from unittest import TestCase


class TestChargeConfig(TestCase):
    def setUp(self) -> None:
        self.configurations = JoulesupChargeConfigurations()
    
    # Test configuration 1
    def test_config_one(self):
        config_1: ChargingConfig = self.configurations.LEVEL_1
        self.assertEqual(config_1.get_config_number(), "1", msg = "Config 1 should have the number '1'")
        self.assertEqual(config_1.get_config_level(), "AC Trickle Charging", msg = "Config 1 should have the level 'AC Trickle Charging'")
        self.assertAlmostEqual(config_1.get_voltage(), 240, msg = "Config 1 should have the voltage 240")
        self.assertAlmostEqual(config_1.get_amperage(), 10.0, msg = "Config 1 should have the amperage 10")
        self.assertAlmostEqual(config_1.get_power(), 2.0, msg = "Config 1 should have a base power of 2")
        self.assertAlmostEqual(config_1.get_base_price(), 5.00, msg = "Config 1 should have a base price of $5.00")
        self.assertEqual(config_1.get_config_name(), "Configuration 1 - AC Trickle Charging")
        comparisonDict = {"number": "1", "description": "Configuration 1 - AC Trickle Charging"}
        self.assertDictEqual(config_1.get_form_json(), comparisonDict)
        
    def test_config_two(self):
        config_2: ChargingConfig = self.configurations.LEVEL_2
        self.assertEqual(config_2.get_config_number(), "2", msg = "Config 1 should have the number '1'")
        self.assertEqual(config_2.get_config_level(), "AC Fast Charging", msg = "Config 2 should have the level 'AC Fast Charging'")
        self.assertAlmostEqual(config_2.get_voltage(), 240, msg = "Config 2 should have the voltage 240")
        self.assertAlmostEqual(config_2.get_amperage(), 16.0, msg = "Config 2 should have the amperage 16")
        self.assertAlmostEqual(config_2.get_power(), 3.6, msg = "Config 2 should have a base power of 3.6")
        self.assertAlmostEqual(config_2.get_base_price(), 7.50, msg = "Config 2 should have a base price of $7.50")
        self.assertEqual(config_2.get_config_name(), "Configuration 2 - AC Fast Charging")
        comparisonDict = {"number": "2", "description": "Configuration 2 - AC Fast Charging"}
        self.assertDictEqual(config_2.get_form_json(), comparisonDict)

    def test_config_three(self):
        config_3: ChargingConfig = self.configurations.LEVEL_3
        self.assertEqual(config_3.get_config_number(), "3", msg = "Config 1 should have the number '1'")
        self.assertEqual(config_3.get_config_level(), "AC Fast Charging", msg = "Config 3 should have the level 'AC Fast Charging'")
        self.assertAlmostEqual(config_3.get_voltage(), 240, msg = "Config 3 should have the voltage 240")
        self.assertAlmostEqual(config_3.get_amperage(), 32.0, msg = "Config 3 should have the amperage 32")
        self.assertAlmostEqual(config_3.get_power(), 7.2, msg = "Config 3 should have a base power of 7.2")
        self.assertAlmostEqual(config_3.get_base_price(), 10.00, msg = "Config 1 should have a base price of $10.00")
        self.assertEqual(config_3.get_config_name(), "Configuration 3 - AC Fast Charging")
        comparisonDict = {"number": "3", "description": "Configuration 3 - AC Fast Charging"}
        self.assertDictEqual(config_3.get_form_json(), comparisonDict)
    
    def test_config_four(self):
        config_4: ChargingConfig = self.configurations.LEVEL_4
        self.assertEqual(config_4.get_config_number(), "4", msg = "Config 1 should have the number '1'")
        self.assertEqual(config_4.get_config_level(), "AC Fast Charging", msg = "Config 4 should have the level 'AC Fast Charging'")
        self.assertAlmostEqual(config_4.get_voltage(), 415, msg = "Config 4 should have the voltage 415")
        self.assertAlmostEqual(config_4.get_amperage(), 16.0, msg = "Config 4 should have the amperage 16")
        self.assertAlmostEqual(config_4.get_power(), 11, msg = "Config 4 should have a base power of 11")
        self.assertAlmostEqual(config_4.get_base_price(), 12.50, msg = "Config 4 should have a base price of $12.50")
        self.assertEqual(config_4.get_config_name(), "Configuration 4 - AC Fast Charging")
        comparisonDict = {"number": "4", "description": "Configuration 4 - AC Fast Charging"}
        self.assertDictEqual(config_4.get_form_json(), comparisonDict)
    
    def test_config_five(self):
        config_5: ChargingConfig = self.configurations.LEVEL_5
        self.assertEqual(config_5.get_config_number(), "5", msg = "Config 5 should have the number '5'")
        self.assertEqual(config_5.get_config_level(), "AC Fast Charging", msg = "Config 5 should have the level 'AC Fast Charging'")
        self.assertAlmostEqual(config_5.get_voltage(), 415, msg = "Config 5 should have the voltage 415")
        self.assertAlmostEqual(config_5.get_amperage(), 32, msg = "Config 5 should have the amperage 32")
        self.assertAlmostEqual(config_5.get_power(), 22, msg = "Config 5 should have a base power of 22")
        self.assertAlmostEqual(config_5.get_base_price(), 15.00, msg = "Config 5 should have a base price of $15.00")
        self.assertEqual(config_5.get_config_name(), "Configuration 5 - AC Fast Charging", msg = "config 5 should have the name 'Configuration 5 - AC Fast Charging'")
        comparisonDict = {"number": "5", "description": "Configuration 5 - AC Fast Charging"}
        self.assertDictEqual(config_5.get_form_json(), comparisonDict)
    
    

    def test_config_six(self):
        config_6: ChargingConfig = self.configurations.LEVEL_6
        self.assertEqual(config_6.get_config_number(), "6", msg = "Config 6 should have the number '6'")
        self.assertEqual(config_6.get_config_level(), "DC Rapid Charging")
        self.assertAlmostEqual(config_6.get_voltage(), 450, msg = "Config 6 should have the voltage 450")
        self.assertAlmostEqual(config_6.get_amperage(), 80, msg = "Config 6 should have the amperage 80")
        self.assertAlmostEqual(config_6.get_power(), 36, msg = "Config 6 should have a base power of 26")
        self.assertAlmostEqual(config_6.get_base_price(), 20, msg = "Config 1 should have a base price of $5")
        self.assertEqual(config_6.get_config_name(), "Configuration 6 - DC Rapid Charging")
        comparisonDict = {"number": "6", "description": "Configuration 6 - DC Rapid Charging"}
        self.assertDictEqual(config_6.get_form_json(), comparisonDict)

    def test_config_seven(self):
        config_7: ChargingConfig = self.configurations.LEVEL_7
        self.assertEqual(config_7.get_config_number(), "7", msg = "Config 7 should have the number '7'")
        self.assertEqual(config_7.get_config_level(), "DC Rapid Charging")
        self.assertAlmostEqual(config_7.get_voltage(), 450, msg = "Config 7 should have the voltage 450")
        self.assertAlmostEqual(config_7.get_amperage(), 200, msg = "Config 7 should have the amperage 200")
        self.assertAlmostEqual(config_7.get_power(), 90, msg = "Config 7 should have a base power of 90")
        self.assertAlmostEqual(config_7.get_base_price(), 30, msg = "Config 1 should have a base price of $5")
        self.assertEqual(config_7.get_config_name(), "Configuration 7 - DC Rapid Charging")
        comparisonDict = {"number": "7", "description": "Configuration 7 - DC Rapid Charging"}
        self.assertDictEqual(config_7.get_form_json(), comparisonDict)
    
    def test_config_eight(self):
        config_8: ChargingConfig = self.configurations.LEVEL_8
        self.assertEqual(config_8.get_config_number(), "8", msg = "Config 8 should have the number '8'")
        self.assertEqual(config_8.get_config_level(), "DC Rapid Charging")
        self.assertAlmostEqual(config_8.get_voltage(), 500, msg = "Config 8  should have the voltage 500")
        self.assertAlmostEqual(config_8.get_amperage(), 700, msg = "Config 8 should have the amperage 700")
        self.assertAlmostEqual(config_8.get_power(), 350 , msg = "Config 9 should have a base power of 350")
        self.assertAlmostEqual(config_8.get_base_price(), 50, msg = "Config 1 should have a base price of $5")
        self.assertEqual(config_8.get_config_name(), "Configuration 8 - DC Rapid Charging")
        comparisonDict = {"number": "8", "description": "Configuration 8 - DC Rapid Charging"}
        self.assertDictEqual(config_8.get_form_json(), comparisonDict)
    
    def test_get_configs(self):
        config_list = self.configurations.get_configs()
        self.assertEqual(config_list[0], self.configurations.LEVEL_1, msg = "Configuration 1 should be in index 0")
        self.assertEqual(config_list[1], self.configurations.LEVEL_2, msg = "Configuration 2 should be in index 1")
        self.assertEqual(config_list[2], self.configurations.LEVEL_3, msg = "Configuration 3 should be in index 2")
        self.assertEqual(config_list[3], self.configurations.LEVEL_4, msg = "Configuration 4 should be in index 3")
        self.assertEqual(config_list[4], self.configurations.LEVEL_5, msg = "Configuration 5 should be in index 4")
        self.assertEqual(config_list[5], self.configurations.LEVEL_6, msg = "Configuration 6 should be in index 5")
        self.assertEqual(config_list[6], self.configurations.LEVEL_7, msg = "Configuration 7 should be in index 6")
        self.assertEqual(config_list[7], self.configurations.LEVEL_8, msg = "Configuration 8 should be in index 7")
    
    def test_get_config(self):
        self.assertEqual(self.configurations.get_config("1"), self.configurations.LEVEL_1, msg = "get_config(1) should return config 1")
        self.assertEqual(self.configurations.get_config("2"), self.configurations.LEVEL_2, msg = "get_config(2) should return config 2")
        self.assertEqual(self.configurations.get_config("3"), self.configurations.LEVEL_3, msg = "get_config(3) should return config 3")
        self.assertEqual(self.configurations.get_config("4"), self.configurations.LEVEL_4, msg = "get_config(4) should return config 4")
        self.assertEqual(self.configurations.get_config("5"), self.configurations.LEVEL_5, msg = "get_config(5) should return config 5")
        self.assertEqual(self.configurations.get_config("6"), self.configurations.LEVEL_6, msg = "get_config(6) should return config 6")
        self.assertEqual(self.configurations.get_config("7"), self.configurations.LEVEL_7, msg = "get_config(7) should return config 7")
        self.assertEqual(self.configurations.get_config("8"), self.configurations.LEVEL_8, msg = "get_config(8) should return config 8")

        with self.assertRaises(InvalidConfigException):
            self.configurations.get_config("9")
    
    def test_get_form_json(self):
        """
        This method has for the most part been tested in the methods 
        - test_get_configs
        - Individual configs 
        Therefore just ensuring that the conversion has converted on one obj
        will satisfy with 100% branch coverage.
        """
        self.assertEqual(self.configurations.get_form_json()[0], self.configurations.LEVEL_1.get_form_json(), 
            msg = "Configuration 1's form json should be in index 0")

    
