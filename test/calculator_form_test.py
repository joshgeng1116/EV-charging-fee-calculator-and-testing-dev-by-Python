from app.calculator_form import Calculator_Form
import unittest
from flask import Flask, request
import os


class Calculator_FormTest(unittest.TestCase):
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    def test_battery_capacity_invalid(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_BatteryPackCapacity("ac/vdsx%")
                self.assertEqual(
                    "Battery Capacity can only contain numbers > 0.",
                    str(cm.exception)
                )

    def test_battery_capacity_negative(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_BatteryPackCapacity(-1)
                self.assertEqual(
                    "Battery cannot have a negative capacity",
                    str(cm.exception)
                )

    def test_battery_capacity_zero(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_BatteryPackCapacity("0")
                self.assertEqual(
                    "Battery cannot have a capacity of zero",
                    str(cm.exception)
                )

    def test_initialCharge_invalid(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_InitialCharge("sankmjdasjmhb")
                self.assertEqual(
                    "Battery state can only contain numbers from 0 to 100.",
                    str(cm.exception)
                )

    def test_initialCharge_negative(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_InitialCharge("-1")
                self.assertEqual(
                    "Initial state of battery is not valid.",
                    str(cm.exception)
                )

    def test_initialCharge_full(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_InitialCharge("100")
                self.assertEqual(
                    "Battery cannot be charged since the Initial state of battery is full.",
                    str(cm.exception)
                )

    def test_initialCharge_overload(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_InitialCharge("101")
                self.assertEqual(
                    "Invalid input, battery state cannot over 100%",
                    str(cm.exception)
                )

    def test_initialCharge_over_finalCharge(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.FinalCharge.data = 2
                    self.mock_Calculator_Form.validate_InitialCharge(50)
                self.assertEqual(
                    "Initial charge data error",
                    str(cm.exception)
                )

    def test_finalCharge_invalid(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_FinalCharge("sankmjdasjmhb")
                self.assertEqual(
                    "Battery state can only contain numbers from 0 to 100.",
                    str(cm.exception)
                )

    def test_finalCharge_negative(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_FinalCharge("-1")
                self.assertEqual(
                    "Final state of battery is not valid.",
                    str(cm.exception)
                )

    def test_finalCharge_overload(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_FinalCharge("101")
                self.assertEqual(
                    "Invalid input, battery state cannot over 100%",
                    str(cm.exception)
                )

    def test_finalCharge_lower_initialCharge(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.InitialCharge.data = 75
                    self.mock_Calculator_Form.validate_FinalCharge(20)
                self.assertEqual(
                    "Final charge data error",
                    str(cm.exception)
                )

    def test_startDate_before2008(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_StartDate('20/08/2007')
                self.assertEqual(
                    "Year of start date should be after 2008",
                    str(cm.exception)
                )

    def test_startDate_after_today(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_StartDate('20/08/2050')
                self.assertEqual(
                    "Start date should before today",
                    str(cm.exception)
                )

    def test_startTime_error(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_StartTime("26:88")
                self.assertEqual(
                    "Start time in wrong form",
                    str(cm.exception)
                )

    def test_chargerConfiguration_error(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_ChargerConfiguration("10")
                self.assertEqual(
                    "Invalid charging configuration",
                    str(cm.exception)
                )

    def test_postCode_error(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    self.mock_Calculator_Form.validate_PostCode("80305")
                self.assertEqual(
                    "Post code not found",
                    str(cm.exception)
                )



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_FormTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
