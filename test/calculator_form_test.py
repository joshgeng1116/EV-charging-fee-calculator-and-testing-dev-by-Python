from app.calculator_form import Calculator_Form
import unittest
from unittest.mock import Mock


class Calculator_FormTest(unittest.TestCase):

    def test_all_none_input(self):
        self.mock_Calculator_Form = Mock()
        self.mock_Calculator_Form.side_effect = ValueError("Battery cannot have a negative capacity")
        self.mock_Calculator_Form.validate_BatteryPackCapacity(self.mock_Calculator_Form, -1)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_FormTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
