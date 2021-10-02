from app.calculator_form import Calculator_Form
import unittest
from flask import Flask, request
from datetime import date
import os


class test_Field():
    def __init__(self, data):
        self.data = data


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
                    field = test_Field(data="ac/vdsx%")
                    self.mock_Calculator_Form.validate_BatteryPackCapacity(field)
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
                    field = test_Field(data="-1")
                    self.mock_Calculator_Form.validate_BatteryPackCapacity(field)
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
                    field = test_Field(data='0')
                    self.mock_Calculator_Form.validate_BatteryPackCapacity(field)
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
                    field = test_Field(data='sankmjdasjmhb')
                    self.mock_Calculator_Form.validate_InitialCharge(field)
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
                    field = test_Field(data="-1")
                    self.mock_Calculator_Form.validate_InitialCharge(field)
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
                    field = test_Field(data="100")
                    self.mock_Calculator_Form.validate_InitialCharge(field)
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
                    field = test_Field(data="101")
                    self.mock_Calculator_Form.validate_InitialCharge(field)
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
                    field = test_Field(data='50')
                    self.mock_Calculator_Form.validate_InitialCharge(field)
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
                    field = test_Field(data='sankmjdasjmhb')
                    self.mock_Calculator_Form.validate_FinalCharge(field)
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
                    field = test_Field(data='-1')
                    self.mock_Calculator_Form.validate_FinalCharge(field)
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
                    field = test_Field(data='101')
                    self.mock_Calculator_Form.validate_FinalCharge(field)
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
                    field = test_Field(data="20")
                    self.mock_Calculator_Form.validate_FinalCharge(field)
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
                    field = test_Field(data=date.fromisoformat('2007-08-20'))
                    self.mock_Calculator_Form.validate_StartDate(field)
                self.assertEqual(
                    "Year of start date should be after 2008",
                    str(cm.exception)
                )



    def test_chargerConfiguration_error(self):
        with self.app.app_context():
            with self.app.test_request_context('/hello', method='POST'):
                assert request.path == '/hello'
                assert request.method == 'POST'
                self.mock_Calculator_Form = Calculator_Form()
                with self.assertRaises(ValueError) as cm:
                    field = test_Field(data="10")
                    self.mock_Calculator_Form.validate_ChargerConfiguration(field)
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
                    field = test_Field(data="80305")
                    self.mock_Calculator_Form.validate_PostCode(field)
                self.assertEqual(
                    "Post code not found",
                    str(cm.exception)
                )


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_FormTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
