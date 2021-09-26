
from flask import config
from typing import Dict, List


class ChargingConfig():

    def __init__(self, config_num: str, config_level: str, voltage: float, 
        amperage: float, power: float, base_price: float):

        self._config_num = config_num
        self._config_level = config_level
        self._voltage = voltage
        self._amperage = amperage
        self._power = power
        self._base_price = base_price

    def get_config_number(self) -> str:
        return self._config_num

    def get_config_level(self) -> str:
        return self._config_level

    def get_voltage(self) -> float:
        return self._voltage

    def get_amperage(self) -> float:
        return self._amperage

    def get_power(self) -> float:
        return self._power

    def get_base_price(self) -> float:
        return self._base_price
    
    def get_config_name(self) -> str:
        return f"Configuration {self.get_config_number()} - {self.get_config_level()}"
    
    def get_form_json(self) -> Dict[str, str]:
        return {"number": self.get_config_number(), "description": self.get_config_name()}
    

class InvalidConfigException(Exception):
    pass

class JoulesupChargeConfigurations:
    LEVEL_1 = ChargingConfig("1", "AC Trickle Charging", 240, 10, 2.0, 5)
    LEVEL_2 = ChargingConfig("2", "AC Fast Charging", 240,  16, 3.6, 7.5)
    LEVEL_3 = ChargingConfig("3", "AC Fast Charging", 240,  32, 7.2, 10)
    LEVEL_4 = ChargingConfig("4", "AC Fast Charging", 415,  16, 11, 12.5)
    LEVEL_5 = ChargingConfig("5", "AC Fast Charging", 415,  32, 22, 15.00)
    LEVEL_6 = ChargingConfig("6", "DC Rapid Charging", 450, 80, 36, 20)
    LEVEL_7 = ChargingConfig("7", "DC Rapid Charging", 450, 200, 90, 30)
    LEVEL_8 = ChargingConfig("8", "DC Rapid Charging", 500, 700, 350, 50)
    
    def get_configs(self) -> List[ChargingConfig]:
        return [self.LEVEL_1, self.LEVEL_2, self.LEVEL_3, self.LEVEL_4,
            self.LEVEL_5, self.LEVEL_6, self.LEVEL_7, self.LEVEL_8]
        
    def get_form_json(self) -> List[Dict[str, str]]:
        return [config.get_form_json() for config in self.get_configs()]
    
    def get_config(self, config_number) -> ChargingConfig:
        if (config_number == self.LEVEL_1.get_config_number()):
            return self.LEVEL_1
        elif (config_number == self.LEVEL_2.get_config_number()):
            return self.LEVEL_2
        elif (config_number == self.LEVEL_3.get_config_number()):
            return self.LEVEL_3
        elif (config_number == self.LEVEL_4.get_config_number()):
            return self.LEVEL_4
        elif (config_number == self.LEVEL_5.get_config_number()):
            return self.LEVEL_5
        elif (config_number == self.LEVEL_6.get_config_number()):
            return self.LEVEL_6
        elif (config_number == self.LEVEL_7.get_config_number()):
            return self.LEVEL_7
        elif (config_number == self.LEVEL_8.get_config_number()):
            return self.LEVEL_8
        else:
            raise InvalidConfigException
