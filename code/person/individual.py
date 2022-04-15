# TODO: METER INDIVIDUAL EN EL INIT

class Individual:
    def __init__(self, individual):
        self._name = individual["name"]
        self._surname = individual["surname"]
        self._passport = individual["passport"]

    @property
    def full_description(self):
        return {"name": self.name, "surname": self.surname, "passport": self.passport}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, new_passport):
        self._passport = new_passport
