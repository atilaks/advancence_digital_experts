from . import Individual


class Owner(Individual):
    def __init__(self, ind, bikes):
        super().__init__(ind)
        self._bikes = bikes

# TODO: LOS TEST FALLAN PORQUE FALTA EL ARGUMENTO BIKE
    def bike_description(self, bike):
        return self._bikes[bike].full_description

    # def get_bike(self, bike):
    #     return self._bikes[bike]
