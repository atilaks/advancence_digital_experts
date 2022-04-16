class ComplaintCounter:
    def __init__(self):
        self._id_complaint = 1

    def counter(self):
        new_id = self._id_complaint
        self._id_complaint += 1
        return new_id
