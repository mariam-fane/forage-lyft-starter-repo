import datetime
from battery.model.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        
        # today = datetime.today().date()
        # self.current_date = today
        
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2) # in two years
        if service_threshold_date < self.current_date :
            return True
        else:
            return False