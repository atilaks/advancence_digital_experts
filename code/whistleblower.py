class Whistleblower:
    def __init__(self, bike, complaint):
        self._whistleblower = {"complaint": "", "license": "", "color": "", "type": "", "status": "",
                               "owner": "", "date": "", "description": "", "address": ""}
        self._bike = bike
        self._complaint = complaint

    def set_whistleblower(self, test):               # REFACTORIZAR
        counter = 0
        for i in self._whistleblower.keys():
            self._whistleblower[i] = test[counter]
            counter += 1

    def get_whistleblower(self):
        return self._whistleblower

