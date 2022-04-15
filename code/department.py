class Department:

    def __init__(self):
        self._department = ["departmentA", "departmentB"]
        self.available_department = True
        self.available_agents = []
        self.not_available_agents = []

    def set_department(self, new_department):
        self._department.append(new_department)

    def get_department(self):
        return self._department

    def set_available_agent(self, agent_id):
        self.available_agents.append(agent_id)
        self.not_available_agents.remove(agent_id)

    def get_available_list(self):
        return self.available_agents

    def set_not_available_agent(self, agent_id):
        self.not_available_agents.append(agent_id)
        self.available_agents.remove(agent_id)

    def get_not_available_list(self):
        return self.not_available_agents
