from . import Individual


class Agent(Individual):
    def __init__(self, agent):
        super().__init__(agent)
        self._police_id = agent["police id"]
        self._department = agent["department"]
        self._range = agent["range"]

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
