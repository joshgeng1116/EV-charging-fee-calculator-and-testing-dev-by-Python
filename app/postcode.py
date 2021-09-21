class Postcode:
    def __init__(self, postcode: str) -> None:
        if len(postcode) == 4:
            self._postcode = postcode 
        else:
            raise ValueError
    
    def __is_nsw(self) -> bool:
        # 1000 - 1999
        if ("1000" <= self._postcode and self._postcode <= "1999"):
            return True
        # 2000 - 2599
        elif ("2000" <= self._postcode and self._postcode <= "2599"):
            return True
        # 2619—2899
        elif ("2619" <= self._postcode and self._postcode <= "2899"):
            return True
        # 2921—2999
        elif ("2921" <= self._postcode and self._postcode <= "2999"):
            return True
        else:
            return False

    def __is_act(self) -> bool:
        # 0200—0299 (LVRs and PO Boxes only)
        if ("0200" <= self._postcode and self._postcode <= "0299"):
            return True
        # 2600—2618
        elif ("2600" <= self._postcode and self._postcode <= "2618"):
            return True
        # 2900—2920
        elif ("2900" <= self._postcode and self._postcode <= "2920"):
            return True
        else:
            return False
    def __is_vic(self) -> bool:
        # 3000—3999
        if ("3000" <= self._postcode and self._postcode <= "3999"):
            return True
        # 8000—8999 (LVRs and PO Boxes only)
        elif ("8000" <= self._postcode and self._postcode <= "8999"):
            return True
        else:
            return False

    def __is_qld(self) -> bool:
        # 4000—4999
        if ("4000" <= self._postcode and self._postcode <= "4999"):
            return True
        # 9000—9999 (LVRs and PO Boxes only)
        elif ("9000" <= self._postcode and self._postcode <= "9999"):
            return True
        else:
            return False
    
    def __is_sa(self) -> bool:
        # 5000 - 5999
        if ("5000" <= self._postcode and self._postcode <= "5999"):
            return True
        else:
            return False

    def __is_wa(self) -> bool:
        # 6000 - 6999
        if ("6000" <= self._postcode and self._postcode <= "6999"):
            return True
        else:
            return False
    
    def __is_tas(self) -> bool:
        # 7000 - 7999
        if ("7000" <= self._postcode and self._postcode <= "7999"):
            return True
        else:
            return False
    
    def __is_nt(self) -> bool:
        # 0800 - 0999
        if ("0800" <= self._postcode and self._postcode <= "0999"):
            return True
        else: 
            return False
    
    def get_postcode(self) -> str:
        return self._postcode
        
    def get_state(self) -> str:
        if self.__is_nsw():
            return "NSW"
        elif self.__is_act():
            return "ACT"
        elif self.__is_vic():
            return "VIC"
        elif self.__is_qld():
            return "QLD"
        elif self.__is_sa():
            return "SA"
        elif self.__is_wa():
            return "WA"
        elif self.__is_tas():
            return "TAS"
        elif self.__is_nt():
            return "NT"
        else:
            raise InvalidPostcodeException("Invalid Postcode")
      


class InvalidPostcodeException(Exception):
    pass