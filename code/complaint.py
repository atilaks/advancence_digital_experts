class Complaint:
    def __init__(self, date, address, id_complaint, description="sin descripción", status="desaparecida"):
        self._date = date
        self._address = address
        self._id_complaint = id_complaint
        self._description = description
        self._status = status

# TODO: HACER QUE LA ID LA GENERE ALEATORIAMENTE

    @property
    def full_description(self):
        return {"date": self.date, "address": self.address, "description": self.description,
                "status": self.status, "id_complaint": self.id_complaint}

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
