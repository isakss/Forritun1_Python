
class Employee(object):
    def __init__(self, employee_name = ""):
        self._employee_name = employee_name
    
    def get_name(self):
        return self._employee_name


class HourlyEmployee(Employee):
    EXCESS_RATE = 1.5

    def __init__(self, employee_name = "", hourly_wages = 0.0):
        super().__init__(employee_name)
        self.hourly_wages = hourly_wages

    def weekly_pay(self, hours):
        if hours > 40:
            return (self.hourly_wages * 40) + ((self.hourly_wages * self.EXCESS_RATE) * (hours - 40))
        else:
            return self.hourly_wages * 40
    
class SalariedEmployee(Employee):
    WEEKS_IN_YEAR = 52

    def __init__(self, employee_name = "", annual_salary = 0.0):
        super().__init__(employee_name)
        self.annual_salary = annual_salary
    
    def weekly_pay(self, hours):
        return self.annual_salary / self.WEEKS_IN_YEAR
    
class Manager(SalariedEmployee):
    def __init__(self, employee_name = "", annual_salary = 0.0, weekly_bonus = 0.0):
        super().__init__(employee_name, annual_salary)
        self.weekly_bonus = weekly_bonus
    
    def weekly_pay(self, hours):
        return (self.annual_salary / self.WEEKS_IN_YEAR) + self.weekly_bonus



    
