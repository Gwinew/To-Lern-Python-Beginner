from datetime import date, timedelta

class Prescription:
    def __init__(self, name, dispense_date, days,supply):
        self.name = name
        self.dispense_date = dispense_date
        self.days_supply = days_supply

    def days_takien(self):
        all_days = (self.despense_date + timedelta(days = i)
                    for i in range(self.days_suplly))
        #return (day for day in all_days if day < date.today())
        return all_days                                             # No limit about days
