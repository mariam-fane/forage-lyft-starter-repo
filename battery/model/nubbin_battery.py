import datetime
from battery.model.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        
        # today = datetime.today().date()
        # self.current_date = today
        
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4) # in four years
        if service_threshold_date < self.current_date :
            return True
        else:
            return False