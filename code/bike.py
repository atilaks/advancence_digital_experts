"""Clase Bike: Genera bicicletas.
        - Constructor: Recibe los parámetros descriptivos de la bicicleta.
        - Propiedades:
            + full_description: Devuelve la descripción completa de la bicicleta.
            + license, color, type, description: Contiene un getter para devolver y un setter para otorgar
            el parámetro correspondiente."""


class Bike:
    def __init__(self, license_id, color="sin color", bike_type="sin definir",
                 description="sin descripción"):
        self._license = license_id
        self._color = color
        self._type = bike_type
        self._description = description

    @property
    def full_description(self):
        return {"license_id": self.license, "color": self.color, "bike_type": self.type,
                "description": self.description}

    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, new_license):
        self._license = new_license

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        self._type = new_type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description
