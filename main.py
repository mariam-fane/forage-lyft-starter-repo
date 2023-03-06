
from datetime import datetime

from car_factory import CarFactory


def calliope_test_battery_should_be_serviced():
    today = datetime.today().date()
    current_date = today
    last_service_date = today.replace(year=today.year - 3)
    current_mileage = 0
    last_service_mileage = 0

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    return car


def test_battery_should_not_be_serviced():
    today = datetime.today().date()
    current_date = today
    last_service_date = today.replace(year=today.year - 1)
    current_mileage = 0
    last_service_mileage = 0

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    return car

def test_engine_should_be_serviced():
    last_service_date = datetime.today().date()
    current_mileage = 30001
    last_service_mileage = 0

    car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
    return car

def test_engine_should_not_be_serviced():
    last_service_date = datetime.today().date()
    current_mileage = 30000
    last_service_mileage = 0

    car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
    return car




if __name__ == "__main__":
    print("welcome")
    car = calliope_test_battery_should_be_serviced()
    print(car.needs_service())
    car = test_battery_should_not_be_serviced()
    print(car.needs_service())
    car = test_engine_should_be_serviced()
    print(car.needs_service())
    car = test_engine_should_not_be_serviced()
    print(car.needs_service())