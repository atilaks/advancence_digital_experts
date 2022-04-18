from . import Individual

"""Clase Owner: Clase con herencia de Individual que genera individuos con rol de propietario.
        - Constructor: Recibe datos de individuo mas los datos de una bicicleta almacenados en un diccionario.
        - Métodos:
            + bike_description: Devuelve la descripción completa de la bici consultada.
            + last_bike: Devuelve la última bici registrada por el propietario.
            + bike_by_license_id: Devuelve la llave del diccionario correspondiente a la identificación de bici."""


class Owner(Individual):
    def __init__(self, bikes, name, surname, passport="sin registro"):
        super().__init__(name, surname, passport)
        self._bikes = bikes

    def bike_description(self, bike):
        return self._bikes[bike].full_description

    def last_bike(self):
        key = 0
        for i in reversed(self._bikes.keys()):
            key = i
            break
        return self._bikes[key].full_description

    def bike_by_license_id(self, license_id):
        for key in self._bikes:
            if self._bikes[key].license is license_id:
                return self._bikes[key]
