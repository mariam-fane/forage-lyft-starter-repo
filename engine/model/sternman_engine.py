from engine.model.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on
    def needs_service(self):
        #  Only when the warning indicator is on 
        if self.warning_light_on:
            return True
        else:
            return False
