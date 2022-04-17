class CoreDepartment:
    def __init__(self, deparments):
        self._department_availability = []
        self._department_unavailability = []
        self._departments = deparments

    def assign_complaint(self, agent, complaint):
        pass

    @property
    def departments(self):
        return self._departments

    def add_department(self, key, department):
        self._departments[key] = department

    @property
    def department_availability(self):
        return self._department_availability

    # @department_availability.setter
    # def department_availability(self, new_department):
    #     self._department_availability.append(new_department)

    # def _add_department_to_list(self, department_key, new_department):
    #     self._department_availability[department_key] = new_department
    #     print(self._department_availability)

# TODO: UTILIZAR LA LOGICA DE DEPARTAMENTO CON AGENTS PARA HACER CORE CON DEPARTAMENTOS

# TODO: MIRAR CON _COMPLAINTS DEL DEPARTAMENTO. CAMBIAR AGENTE POR DEPARTAMENTO(diccionario con las keys como departamento)
# TODO: DICCIONARIO DE TODOS LOS DEPARTAMENTOS Y DICCIONARIO DE DENUNCIAS CON LAS KEYS DE LOS DEPARTAMENTOS
# TODO: BUSCAR A PARTIR DE LA BICI(ID) EL NUMERO DE DENUNCIA (es el punto 6)