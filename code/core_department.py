class CoreDepartment:

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

# TODO: FALTA TODO
