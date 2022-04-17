from code import DepartmentWithActiveComplaintsException, NotAvailableDepartmentsException, ComplaintNotFoundException


class CoreDepartment:
    def __init__(self, deparments):
        self._department_availability = []
        self._department_unavailability = []
        self._departments = {}
        self._complaints = {}
        for key in deparments:
            self.add_department(key, deparments[key])

    def assign_complaint(self, complaint):
        for department in self.departments:
            if len(self.departments[department].unassigned_agents) > 0:
                self.departments[department].assign_complaint(complaint)
                self._complaints[department].append(complaint)
                break
        else:
            raise NotAvailableDepartmentsException

    @property
    def departments(self):
        return self._departments

    @property
    def complaints(self):
        return self._complaints

    def add_department(self, key, department):
        self._departments[key] = department
        self._complaints[key] = []

    @property
    def department_availability(self):
        return self._department_availability

    def remove_department_by_name(self, department_name):
        removal = ""
        for key in self._departments:
            if self._departments[key].name == department_name:
                removal = key
                if len(self.complaints[key]) > 0:
                    raise DepartmentWithActiveComplaintsException
        del self._departments[removal]

    def close_complaint(self, id_complaint):
        complaint_to_be_removed = None
        complaint_to_be_removed_key = None
        break_flag = False
        for key in self.complaints:
            for complaint in self.complaints[key]:
                if complaint.id_complaint == id_complaint:
                    self.departments[key].close_complaint(id_complaint)
                    complaint_to_be_removed = complaint
                    complaint_to_be_removed_key = key
                    break_flag = True
                    break
            if break_flag:
                break
        else:
            raise ComplaintNotFoundException
        complaint_to_be_removed.status = "encontrada"
        self.complaints[complaint_to_be_removed_key].remove(complaint_to_be_removed)

    def get_info_by_bike_id(self, bike_id):
        complaint_found = None
        complaint_key = None
        break_flag = False
        for key in self.complaints:
            for complaint in self.complaints[key]:
                if complaint.bike.license == bike_id:
                    complaint_key = key
                    complaint_found = complaint
                    break_flag = True
                    break
            if break_flag:
                break
        else:
            return "La bicicleta no se ha encontrado"
        bike_found_id = complaint_found.bike.license
        complaint_id = complaint_found.id_complaint
        department_name = self.departments[complaint_key].name
        owner_passport = complaint_found.owner.passport
        return {"bike_id": bike_found_id, "complaint_id": complaint_id, "department_name": department_name,
                "owner_passport": owner_passport}


# TODO: BUSCAR A PARTIR DE LA BICI(ID) EL NUMERO DE DENUNCIA (es el punto 6)