from code.person.individual import Individual
# TODO: METER INDIVIDUAL EN EL INIT


class Owner(Individual):
    def __init__(self, individual, bike):
        super().__init__(individual)
        self._bike = bike

    def bike_description(self):
        return self._bike.full_description

# TODO: HACER ESCALABLE A QUE PUEDA TENER VARIAS BICIS (con diccionario). *modificar linea 11

    # @property
    # def bike(self):
    #     return self._bike
    #