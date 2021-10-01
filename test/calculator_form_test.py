from app.calculator_form import Calculator_Form
from app.chargeconfig import JoulesupChargeConfigurations
import unittest


class Calculator_FormTest(unittest.TestCase):
    def all_correct(self):
        form = Calculator_Form(None, None, None, None, None, None, None)
        self.assertEqual(form.BatteryPackCapacity(), 'Field data is none')
        self.assertEqual(form.InitialCharge(), "Initial state of battery not provided")
        self.assertEqual(form.FinalCharge(), "Final state of battery not provided")
        self.assertEqual(form.StartDate(), 'Start date is none')
        self.assertEqual(form.StartTime(), 'Start time is none')
        self.assertEqual(form.ChargerConfiguration(), "Charger configuration should not be None.")
        self.assertEqual(form.PostCode(), "Post code should not be none")


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_FormTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
