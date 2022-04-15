import random


class IncidentManager:

    @staticmethod
    def recorded_incident():
        return "Se ha registrado un el incidente"

    def set_department(self):
        if self.available_department:
            assignment = self.get_random_departments()
        else:
            assignment = "not assigned"
        return assignment

    def get_random_departments(self):
        return self._department[random.randint(0, len(self._department))]

    def set_department_availability(self):
        if self.available_department:
            self.available_department = False
        else:
            self.available_department = True
