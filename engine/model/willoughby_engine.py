from engine.model.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage,current_milage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_milage
    def needs_service(self):
        pass