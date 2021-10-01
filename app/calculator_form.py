"""
FIT2107 2021 Semester 2 - NullPointerException

Date First Modified: 2021-09-10
Date Modified: 2021-00-10

A file which a class called Caluclator_Form that will validate the data
in the Joules Up charging calculator website. 
"""

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Optional
from .postcode import Postcode, InvalidPostcodeException
from .chargeconfig import JoulesupChargeConfigurations, InvalidConfigException
from datetime import date, time


# validation for form inputs
class Calculator_Form(FlaskForm):
    # this variable name needs to match with the input attribute name in the html file
    # you are NOT ALLOWED to change the field type, however, you can add more built-in validators and custom messages
    BatteryPackCapacity = StringField("Battery Pack Capacity", [DataRequired()])
    InitialCharge = StringField("Initial Charge", [DataRequired()])
    FinalCharge = StringField("Final Charge", [DataRequired()])
    StartDate = DateField("Start Date", [DataRequired("Data is missing or format is incorrect")], format='%d/%m/%Y')
    StartTime = TimeField("Start Time", [DataRequired("Data is missing or format is incorrect")], format='%H:%M')
    ChargerConfiguration = StringField("Charger Configuration", [DataRequired()])
    PostCode = StringField("Post Code", [DataRequired()])

    # use validate_ + field_name to activate the flask-wtforms built-in validator
    # this is an example for you
    def validate_BatteryPackCapacity(self, field):
        try:
            float(field)
        except:
            raise ValueError("Battery Capacity can only contain numbers > 0.")
        if float(field) < 0:
            raise ValueError("Battery cannot have a negative capacity")
        elif float(field) == 0:
            raise ValueError("Battery cannot have a capacity of zero")

    # validate initial charge here
    def validate_InitialCharge(self, field):
        # another example of how to compare initial charge with final charge
        # you may modify this part of the code
        try:
            int(field)
        except:
            raise ValueError("Battery state can only contain numbers from 0 to 100.")

        if int(field) < 0:
            raise ValueError("Initial state of battery is not vaild.")
        elif int(field) > self.FinalCharge.data:
            raise ValueError("Initial charge data error")
        elif int(field) == 100:
            raise ValueError("Battery cannot be charged since the Initial state of battery is full.")
        elif int(field) > 100:
            raise ValueError("Invalid input, battery state cannot over 100%")

    # validate final charge here
    def validate_FinalCharge(self, field):
        try:
            int(field)
        except:
            raise ValueError("Battery state can only contain numbers from 0 to 100.")
        if int(field) < 0:
            raise ValueError("Final state of battery is not valid.")
        elif int(field) > self.FinalCharge.data:
            raise ValueError("Final charge data error")
        elif int(field) == 100:
            raise ValueError("Battery cannot be charged since the Final state of battery is full.")
        elif int(field) > 100:
            raise ValueError("Invalid input, battery state cannot over 100%")


    # validate start date here
    def validate_StartDate(self, field):
        try:
            date.fromisoformat(field)
        except:
            raise ValueError("Start date in wrong form")

    # validate start time here
    def validate_StartTime(self, field):
        try:
            time.fromisoformat(field)
        except:
            raise ValueError("Start time in wrong form")

    # validate charger configuration here
    def validate_ChargerConfiguration(self, field):
        try:
            JoulesupChargeConfigurations().get_config(field)
        except InvalidConfigException:
            raise ValueError("Invalid charging configuration")

    # validate postcode here
    def validate_PostCode(self, field):
        try:
            Postcode(field)
        except InvalidPostcodeException:
            raise ValueError("Post code not found")
