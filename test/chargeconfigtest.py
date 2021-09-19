from app.chargeconfig import ChargingConfig
import unittest


class ChargeConfigTest(unittest.TestCase):

    # Test configuration 1
    def test_config_one(self):
        config = ChargingConfig(1, "Level 1", 240, 10, 2.0, 5.0)
        self.assertEqual(config.get_power(), 2)
        self.assertEqual(config.get_base_price(), 5.0)
        self.assertEqual(config.get_config_level(), "Level 1")
        self.assertEqual(config.get_voltage(), 240)
        self.assertEqual(config.get_amperage(), 10)


