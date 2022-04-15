class Bike:

    def __init__(self, bike):
        self._license = bike["license"]
        self._color = bike["color"]
        self._type = bike["type"]
        self._description = bike["description"]

    @property
    def full_description(self):
        return {"license": self._license, "color": self._color, "type": self._type,
                "description": self._description}

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
