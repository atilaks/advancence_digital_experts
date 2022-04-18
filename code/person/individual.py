"""Clase Individual: Clase madre para generar personas con distintos roles.
        - Constructor: Recibe datos genéricos de cualquier individuo.
        - Propiedades:
            + full_description: Devuelve la descripción completa como individuo.
            + name, surname, passport: Cada una contiene un getter para devolver.
              y un setter para otorgar el parámetro correspondiente."""


class Individual:
    def __init__(self, name, surname, passport="sin registro"):
        self._name = name
        self._surname = surname
        self._passport = passport

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
