from . import Individual


class Owner(Individual):
    def __init__(self, bikes, name, surname, passport="sin registro"):
        super().__init__(name, surname, passport)
        self._bikes = bikes

    def bike_description(self, bike):
        return self._bikes[bike].full_description

    # def get_bike(self, bike):
    #     return self._bikes[bike]
