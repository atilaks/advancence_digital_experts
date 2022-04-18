from . import Agent

"""Clase DepartmentManager: Clase con herencia de Agent que genera individuos con rol de jefe de departamento.
        - Constructor: Recibe datos de individuo mas los datos correspondientes a policía.
        - Propiedades: 
            + department, manager: Contiene un getter para devolver y un setter para otorgar el parámetro 
              correspondiente."""


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
