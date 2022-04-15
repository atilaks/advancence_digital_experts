from . import Individual


class Owner(Individual):
    def __init__(self, ind, bike):
        super().__init__(ind)
        self._bike = bike

    def bike_description(self):
        return self._bike.full_description

# TODO: HACER ESCALABLE A QUE PUEDA TENER VARIAS BICIS (con diccionario). *modificar linea 11
