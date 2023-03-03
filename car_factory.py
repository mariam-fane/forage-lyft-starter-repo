from battery.model.spindler_battery import SpindlerBattery
from engine.model.capulet_engine import CapuletEngine
from car import Car


class CarFactory():

    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        ce =  CapuletEngine(last_service_mileage, current_mileage)
        bat = SpindlerBattery(last_service_date,current_date)
        car = Car(ce,bat)
        return car