from app.chargeconfig import ChargingConfig, JoulesupChargeConfigurations
from app.postcode import Postcode
from app.calculator import Calculator
from datetime import date, time



class CalculatorPresentation:
    CALCULATOR_CLASS = Calculator
    
    def __init__(self, initial_state: str, final_state: str, battery_capacity: str, charger_config: str,
        start_date: date, start_time: time, postcode: str, calculatorClass: Calculator = Calculator) -> None:
        config = JoulesupChargeConfigurations().get_config(charger_config)
        self.calculator = calculatorClass(inital_state = float(initial_state), final_state=float(final_state), 
            capacity=float(battery_capacity), config = config,
            start_date=start_date, start_time=start_time,
            postcode=Postcode(postcode))
    
    def get_time(self) -> str:
        minutes = self.calculator.get_duration_in_minutes()
        if minutes < 60:
            return f"{minutes} Minutes"
        elif minutes >= 60 and minutes % 60 == 0:
            return f"{int(minutes // 60)} Hours"
        else:
            return f"{int(minutes //60)} Hours and {int(minutes % 60)} Minutes"
            
    
    def get_cost(self) -> str:
        return "${:.2f}".format(self.calculator.cost_calculation())
    

    