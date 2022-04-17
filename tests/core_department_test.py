import unittest
from code import CoreDepartment, Department, Agent, Bike, Owner, Complaint, DepartmentWithActiveComplaintsException, \
    NotAvailableDepartmentsException


class TestCoreDepartment(unittest.TestCase):
    def setUp(self) -> None:
        self.agent1 = Agent(name="José", surname="García", passport="56475215f", police_id="A5826",
                            department="departmentA", range="official")
        self.agent2 = Agent(name="Julio", surname="Montero", passport="56564715f", police_id="D5876",
                            department="departmentA", range="comisario")

        agents = {"a1": self.agent1, "a2": self.agent2}

        self.department = Department(name="DepartamentoA", address="calle Las barcas, 8, Alfafar, 46910",
                                     agents=agents)

        self.a_department = {"D1": self.department}

        self.core_department = CoreDepartment(self.a_department)

    def test_how_many_department(self):
        # Arrange
        expected = {"D1": self.department}

        # Act
        departments = self.core_department.departments

        # Assert
        self.assertEqual(expected, departments)

    def test_new_department(self):
        # Arrange
        department2 = Department(name="DepartamentoB", address="calle Las barcas, 8, Alfafar, 46910")
        expected = {"D1": self.department, "D2": department2}

        # Act
        self.core_department.add_department("D2", department2)
        available = self.core_department.departments

        # Assert
        self.assertEqual(expected, available)

    def test_drop_department(self):
        # Arrange
        department2 = Department(name="DepartamentoB", address="calle Las barcas, 8, Alfafar, 46910")
        self.core_department.add_department("D2", department2)
        department_name = "DepartamentoA"
        expected = {"D2": department2}

        # Act
        self.core_department.remove_department_by_name(department_name)
        departments = self.core_department.departments

        # Assert
        self.assertEqual(expected, departments)

    def test_assign_complaint(self):
        # Arrange
        self.bike = Bike(license_id="00001AAA", color="rojo", bike_type="carretera")
        a_bike = {"b1": self.bike}
        owner = Owner(a_bike, name="José", surname="García")
        complaint = Complaint(owner, "00001AAA", date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910", id_complaint=0)

        expected = {'D1': [complaint]}

        # Act
        self.core_department.assign_complaint(complaint)
        assigned = self.core_department.complaints

        # Assert
        self.assertEqual(expected, assigned)

    def test_cannot_drop_department_with_complaints(self):
        # Arrange
        self.bike = Bike(license_id="00001AAA", color="rojo", bike_type="carretera")
        a_bike = {"b1": self.bike}
        owner = Owner(a_bike, name="José", surname="García")
        complaint = Complaint(owner, "00001AAA", date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910", id_complaint=0)
        department_name = "DepartamentoA"

        # Act
        self.core_department.assign_complaint(complaint)

        # Assert
        self.assertRaises(DepartmentWithActiveComplaintsException,
                          lambda: self.core_department.remove_department_by_name(department_name))

    def test_cannot_assign_complaint_if_not_available_departament(self):
        # Arrange
        self.bike = Bike(license_id="00001AAA", color="rojo", bike_type="carretera")
        a_bike = {"b1": self.bike}
        owner = Owner(a_bike, name="José", surname="García")
        complaint1 = Complaint(owner, "00001AAA", date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910", id_complaint=0)
        complaint2 = Complaint(owner, "00001AAA", date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910", id_complaint=1)
        complaint3 = Complaint(owner, "00001AAA", date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910", id_complaint=2)

        # Act
        self.core_department.assign_complaint(complaint1)
        self.core_department.assign_complaint(complaint2)

        # Assert
        self.assertRaises(NotAvailableDepartmentsException,
                          lambda: self.core_department.assign_complaint(complaint3))

    def test_close_complain(self):
        # Arrange
        self.bike = Bike(license_id="00001AAA", color="rojo", bike_type="carretera")
        a_bike = {"b1": self.bike}
        owner = Owner(a_bike, name="José", surname="García", passport="45786912K")
        id_complaint = 0
        complaint = Complaint(owner, "00001AAA", date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910",
                              id_complaint=id_complaint)
        self.core_department.assign_complaint(complaint)
        expected = {'D1': []}

        # Act
        self.core_department.close_complaint(id_complaint)
        assigned = self.core_department.complaints

        # Assert
        self.assertEqual(expected, assigned)
        self.assertEqual(complaint.status, "encontrada")

    def test_info_by_bike_id(self):
        # Arrange
        bike_id = "00001AAA"
        self.bike = Bike(license_id=bike_id, color="rojo", bike_type="carretera")
        a_bike = {"b1": self.bike}
        owner = Owner(a_bike, name="José", surname="García", passport="45786912K")
        complaint = Complaint(owner, bike_id, date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910", id_complaint=0)
        self.core_department.assign_complaint(complaint)
        expected = {"bike_id": bike_id, "complaint_id": 0, "department_name": "DepartamentoA", "owner_passport": "45786912K"}

        # Act
        info = self.core_department.get_info_by_bike_id(bike_id)

        # Assert
        self.assertEqual(expected, info)

    def test_register_complaint(self):
        # Arrange
        bike_id = "00001AAA"
        bike_data = {"license": bike_id, "color": "rojo", "type": "carretera", "name": "bici1"}
        owner_data = {"name": "José", "surname": "García"}
        date = "17/04/2022"
        address = "calle Las barcas, 8, Alfafar, 46910"
        expected = {"bike_id": bike_id, "complaint_id": 0, "department_name": "DepartamentoA",
                    "owner_passport": "sin registro"}

        # Act
        self.core_department.register_complaint(bike_data, owner_data, date, address)
        info = self.core_department.get_info_by_bike_id(bike_id)

        # Assert
        self.assertEqual(expected, info)


if __name__ == '__main__':
    unittest.main()
