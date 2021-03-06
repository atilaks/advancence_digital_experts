import os
from code import ApiGeocode, ComplaintNotFoundException
from dotenv import load_dotenv

"""Clase Department: Genera y gestiona departamentos de policía.
        - Constructor: Recibe datos del departamento y sus agentes asignados.
        - Propiedades: 
            + full_description: Devuelve la descripción completa como departamento.
            + name, address: Contiene un getter para devolver y un setter para otorgar el parámetro correspondiente.
            + agents: Contiene un getter para devolver el parámetro correspondiente.
            + complaints: Devuelve las denuncias.
            + assigned_agents: Devuelve agentes con denuncias.
            + unassigned_agents: Devuelve agentes sin denuncias.
        - Métodos:
            + _set_assigned_agents: Ordena agentes en las listas.
            + assign_agent: Agrega un agente al departamento.
            + remove_agent_by_police_id: Elimina un policía desde la identificación de policía aportada.
            + assign_complaint: Asigna una denuncia a un policía disponible.
            + close_complaint: Cierra una denuncia por la identificación de denuncia aportada.
            + get_coordinates: Devuelve las coordenadas del Departamento."""


class Department:
    def __init__(self, name, address, agents=None):
        if agents is None:
            agents = {}
        self._name = name
        self._address = address
        self._agents = agents
        self._complaints = {}
        self._assigned_agents = []
        self._unassigned_agents = []
        self._lat = None
        self._lng = None
        self._set_assigned_agents()

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

    @property
    def complaints(self):
        return self._complaints

    @property
    def assigned_agents(self):
        return self._assigned_agents

    @property
    def unassigned_agents(self):
        return self._unassigned_agents

    def _set_assigned_agents(self):
        self._assigned_agents = list(self._complaints.keys())
        self._unassigned_agents = []
        for agent_key in self._agents.keys():
            if agent_key not in self.assigned_agents:
                self._unassigned_agents.append(agent_key)

    def assign_agent(self, agent_key, new_agent):
        self._agents[agent_key] = new_agent

    def remove_agent_by_police_id(self, police_id):
        removal = ""
        for key in self._agents:
            if self._agents[key].police_id == police_id:
                removal = key
        del self._agents[removal]

    def assign_complaint(self, complaint):
        if self.unassigned_agents:
            self._complaints[self.unassigned_agents[0]] = complaint
            self._set_assigned_agents()

    def close_complaint(self, id_complaint):
        complaint_to_be_removed = None
        for key in self._complaints:
            if self._complaints[key].id_complaint == id_complaint:
                complaint_to_be_removed = key
                break
        else:
            raise ComplaintNotFoundException
        del self._complaints[complaint_to_be_removed]
        self._set_assigned_agents()

    def get_coordinates(self):
        if self._lat is None and self._lng is None:
            load_dotenv()
            self.token = os.getenv("key_google")
            self.geocode = ApiGeocode(self.token)
            request = self.geocode.get_coordinates(self._address)
            self._lat = request["lat"]
            self._lng = request["lng"]
        return {"lat": self._lat, "lng": self._lng}
