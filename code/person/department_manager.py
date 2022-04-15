from code.person import Agent
# TODO: NO ME DEJA INCORPORAR AGENT DESDE EL PAQUETE CODE


class DepartmentManager(Agent):
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
