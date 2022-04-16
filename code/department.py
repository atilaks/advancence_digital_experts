class Department:
    def __init__(self, name, address, agents={}):
        self._name = name
        self._address = address
        self._agents = agents

#TODO: FALTA ASIGNAR DENUNCIA, CERRAR DENUNCIA Y POLICIAS DISPONIBLES
#TODO: COMO MARCAR LA DISPONIBILIDAD DE LOS POLICIAS??

    @property
    def full_description(self):
        return {"name": self.name, "address": self.address, "agents": self.agents}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    @property
    def agents(self):
        return self._agents

    def assign_agent(self, agent_key, new_agent):
        self._agents[agent_key] = new_agent

    def remove_agent_by_police_id(self, police_id):
        for i in self._agents:
            if self._agents[i]["police_id"] == police_id:
                del self._agents[i]
