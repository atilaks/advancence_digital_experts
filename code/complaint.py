import os
from code import ApiGeocode
from dotenv import load_dotenv


class Complaint:
    def __init__(self, owner, license_id, date, address, id_complaint, description="sin descripción", status="desaparecida"):
        self._owner = owner
        self._bike = None
        self._date = date
        self._address = address
        self._id_complaint = id_complaint
        self._description = description
        self._status = status
        self._lat = None
        self._lng = None
        self._bike_reported(license_id)

# TODO: HACER QUE LA ID LA GENERE ALEATORIAMENTE

    @property
    def full_description(self):
        return {"owner": self._owner.full_description, "bike": self.bike.full_description, "date": self.date, "address": self.address,
                "description": self.description, "status": self.status, "id_complaint": self.id_complaint}

    @property
    def bike(self):
        return self._bike

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address
        self._lat = None
        self._lng = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @property
    def id_complaint(self):
        return self._id_complaint

    def _bike_reported(self, license_id):
        self._bike = self._owner.bike_by_license_id(license_id)

    def get_coordinates(self):
        if self._lat is None and self._lng is None:
            load_dotenv()
            self.token = os.getenv("key_google")
            self.geocode = ApiGeocode(self.token)
            request = self.geocode.get_coordinates(self._address)
            self._lat = request["lat"]
            self._lng = request["lng"]
        return {"lat": self._lat, "lng": self._lng}
