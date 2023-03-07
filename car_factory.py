from battery.model.nubbin_battery import NubbinBattery
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine
from battery.model.spindler_battery import SpindlerBattery
from engine.model.capulet_engine import CapuletEngine
from car import Car


class CarFactory():

# To create calliope
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        # Create Engine: CapuletEngine 
        ce =  CapuletEngine(last_service_mileage, current_mileage)
        # Create battery: SpindlerBattery 
        sb = SpindlerBattery(last_service_date,current_date)
        # create car Calliope 
        car = Car(ce,sb)
        return car

# To create glissade 
    @staticmethod
    def  create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        # create engine: WilloughbyEngine 
        we = WilloughbyEngine(last_service_mileage, current_mileage)
        # create battery 
        sb = SpindlerBattery(last_service_date, current_date)
        # create car Glissade 
        car = Car(we, sb)
        return car

# To create palindrome
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        # create engine: SternmanEngine 
        se = SternmanEngine(warning_light_on)
        # create battery: SpindlerBattery 
        sb = SpindlerBattery(last_service_date, current_date)
        # create car Palindrome 
        car = Car(se, sb)
        return car

# create rorschach 
    @staticmethod
    def  create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage):
        # create engine: WilloughbyEngine 
        we = WilloughbyEngine(last_service_mileage, current_mileage)
        # create battery: NubbinBattery
        nb = NubbinBattery(last_service_date, current_date)
        # create car Rorschach
        car = Car(we, nb)
        return car

# To create Thovex 
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # create engine: CapuletEngine 
        ce = CapuletEngine(last_service_mileage, current_mileage)
        # create NubbinBattery 
        nb = NubbinBattery(last_service_date, current_date)
        # create car Thovex 
        car = Car(ce, nb)
        return car
