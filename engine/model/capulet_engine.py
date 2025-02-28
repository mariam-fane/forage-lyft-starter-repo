

from engine.model.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    def needs_service(self): 
        # Once every 30,000 miles
        return self.current_mileage - self.last_service_mileage > 30000