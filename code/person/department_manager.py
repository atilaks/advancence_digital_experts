from . import Agent


class DepartmentManager(Agent):
    def __init__(self, name, surname, passport, police_id, department, range):
        super().__init__(name, surname, passport, police_id, department, range)

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        self._department = new_department

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, new_status):
        self._manager = new_status
