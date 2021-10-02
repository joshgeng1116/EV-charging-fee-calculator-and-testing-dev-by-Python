"""
FIT2107 2021 Semester 2 - NullPointerException

Date First Modified: 2021-09-10
Date Modified: 2021-00-10

A file which will launch the Joules Up charging calculator and Route requests.
"""

from flask import Flask, flash
from flask import render_template
from flask import request
from datetime import date
from app.calculator import *
from app.calculator_presentation import *
from app.chargeconfig import JoulesupChargeConfigurations as JCC
from app.calculator_form import *
import os
SECRET_KEY = os.urandom(32)

ev_calculator_app = Flask(__name__)
ev_calculator_app.config['SECRET_KEY'] = SECRET_KEY


@ev_calculator_app.route('/', methods=['GET', 'POST'])
def operation_result():
    # request.form looks for:
    # html tags with matching "name="

    calculator_form = Calculator_Form(request.form)

    # validation of the form
    if request.method == "POST" and calculator_form.validate():
        # if valid, create calculator to calculate the time and cost

        # extract information from the form
        battery_capacity = request.form['BatteryPackCapacity']
        initial_charge = request.form['InitialCharge']
        final_charge = request.form['FinalCharge']
        start_date = request.form['StartDate']
        start_time = request.form['StartTime']
        charger_configuration = request.form['ChargerConfiguration']
        postcode = request.form["PostCode"]
        
        start_date_split = start_date.split("/")
        new_start_date = f"{start_date_split[2]}-{start_date_split[1]}-{start_date_split[0]}"

        presentation = CalculatorPresentation(initial_charge, final_charge, battery_capacity, charger_configuration, new_start_date, start_time, postcode, CalculatorWithSolarEnergy)
        duration = presentation.get_time()
        cost = presentation.get_cost()
        # cost = calculator.cost_calculation(initial_charge, final_charge, battery_capacity, is_peak, is_holiday)

        # time = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)

        # you may change the return statement also
        
        # values of variables can be sent to the template for rendering the webpage that users will see
        # return render_template('calculator.html', cost = cost, time = time, calculation_success = True, form = calculator_form)
        return render_template('calculator.html', calculation_success=True, form=calculator_form, configs = JCC().get_form_json(), time=duration, cost=cost)

    else:
        # battery_capacity = request.form['BatteryPackCapacity']
        # flash(battery_capacity)
        # flash("something went wrong")
        flash_errors(calculator_form)
        return render_template('calculator.html', calculation_success = False, form = calculator_form, configs = JCC().get_form_json())

# method to display all errors
def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


if __name__ == '__main__':
    ev_calculator_app.run()
