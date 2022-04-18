from . import Individual

"""Clase Agent: Clase con herencia de Individual que genera individuos con rol de agente de policía.
        - Constructor: Recibe datos de individuo mas los datos correspondientes a policía.
        - Propiedades: 
            + agent_description: Devuelve la descripción completa como policía.
            + all_features: Devuelve la descripción completa como individuo con rol de policía.
            + police_id: Contiene un getter para devolver y un setter para otorgar el parámetro correspondiente.
            + department, range: Contiene un getter para devolver el parámetro correspondiente.
            
    *Los policías no tienen capacidad para cambiar de departamento o rango"""


class Agent(Individual):
    def __init__(self, name, surname, passport, police_id, department, range):
        super().__init__(name, surname, passport)
        self._police_id = police_id
        self._department = department
        self._range = range

    @property
    def agent_description(self):
        return {"police id": self.police_id, "department": self.department, "range": self.range}

    @property
    def all_features(self):
        result = {**self.full_description, **self.agent_description}
        return result

    @property
    def police_id(self):
        return self._police_id

    @police_id.setter
    def police_id(self, new_police_id):
        self._police_id = new_police_id

    @property
    def department(self):
        return self._department

    @property
    def range(self):
        return self._range
