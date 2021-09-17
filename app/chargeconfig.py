from typing import final


class ChargingConfig():

    def __init__(self, config_num, config_level, voltage, amperage, power, base_price):
        self._config_num = config_num
        self._config_level = config_level
        self._voltage = voltage
        self._amperage = amperage
        self._power = power
        self._base_price = base_price

    def get_config_number(self) -> int:
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
