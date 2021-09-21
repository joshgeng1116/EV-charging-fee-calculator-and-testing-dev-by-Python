class Postcode:
    def __init__(self, postcode: str) -> None:
        if len(postcode) == 4:
            self.postcode = postcode 
        else:
            raise ValueError
    
    def __is_nsw(self) -> bool:
        # 1000 - 1999
        if ("1000" <= self.postcode and self.postcode <= "1999"):
            return True
        # 2000 - 2599
        elif ("2000" <= self.postcode and self.postcode <= "2599"):
            return True
        # 2619—2899
        elif ("2619" <= self.postcode and self.postcode <= "2899"):
            return True
        # 2921—2999
        elif ("2921" <= self.postcode and self.postcode <= "2999"):
            return True
        else:
            return False

    def __is_act(self) -> bool:
        # 0200—0299 (LVRs and PO Boxes only)
        if ("0200" <= self.postcode and self.postcode <= "0299"):
            return True
        # 2600—2618
        elif ("2600" <= self.postcode and self.postcode <= "2618"):
            return True
        # 2900—2920
        elif ("2900" <= self.postcode and self.postcode <= "2920"):
            return True
        else:
            return False
    def __is_vic(self) -> bool:
        pass
    def __is_qld(self) -> bool:
        pass
    def __is_sa(self) -> bool:
        pass
    def __is_wa(self) -> bool:
        pass
    def __is_tas(self) -> bool:
        pass
    def __is_nt(self) -> bool:
        pass
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