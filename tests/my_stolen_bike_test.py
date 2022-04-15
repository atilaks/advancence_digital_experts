import unittest
from code import *


bike_description = ["00001AAA", "rojo", "carretera", "desaparecida", "Jose García",
                    "19/03/2022", "sin descripción", "c/Francisco de Goya, 3"]
whistleblower = ["Antonio García", "00001AAA", "rojo", "carretera", "desaparecida", "Jose García",
                 "19/03/2022", "sin descripción", "c/Francisco de Goya, 3"]
agent = ["Roberto Medina", "256478", "departmentX"]


class TestStolenBike(unittest.TestCase):
    def test_define_bike(self):
        # Arrange
        bike = Bike()
        bike.set_bike(bike_description)
        expected = {"license": "00001AAA", "color": "rojo", "type": "carretera",
                    "status": "desaparecida", "owner": "Jose García", "date": "19/03/2022",
                    "description": "sin descripción", "address": "c/Francisco de Goya, 3"}

        # Act
        result = bike.get_bike()

        # Assert
        self.assertEqual(expected, result)

    def test_bike_status(self):
        # Arrange
        status = Bike()
        status.set_bike(bike_description)
        expected = "desaparecida"

        # Act
        result = status.set_status()

        # Assert
        self.assertEqual(expected, result)

    def test_change_status(self):
        # Arrange
        status = Bike()
        status.set_bike(bike_description)
        status.get_status()
        expected = "encontrada"

        # Act
        result = status.set_status()

        # Assert
        self.assertEqual(expected, result)

    def test_bike_address(self):
        # Arrange
        bike = Bike()
        bike.set_bike(bike_description)
        expected = "c/Francisco de Goya, 3"

        # Act
        result = bike.get_address()

        # Assert
        self.assertEqual(expected, result)

    def test_record_incident(self):
        # Arrange
        incident = IncidentManager()
        expected = "Se ha registrado un el incidente"

        # Act
        result = incident.recorded_incident()

        # Assert
        self.assertEqual(expected, result)

    def test_see_department(self):
        # Arrange
        department = Department()
        expected = ["departmentA", "departmentB"]

        # Act
        result = department.get_department()

        # Assert
        self.assertEqual(expected, result)

    def test_add_department(self):
        # Arrange
        new_department = Department()
        new_department.set_department("departmentC")
        expected = ["departmentA", "departmentB", "departmentC"]

        # Act
        result = new_department.get_department()

        # Assert
        self.assertEqual(expected, result)

    def test_available_list(self):
        # Arrange
        list = Department()
        list.set_available_agent("256478")
        expected = ["256478"]

        # Act
        result = list.get_available_list()

        # Assert
        self.assertEqual(expected, result)

    def test_not_available_list(self):
        # Arrange
        list = Department()
        list.set_not_available_agent("256478")
        expected = ["256478"]

        # Act
        result = list.get_not_available_list()

        # Assert
        self.assertEqual(expected, result)

    def test_new_complaint(self):
        # Arrange
        person = Complaint()
        person.set_complaint("Antonio García")
        expected = "Antonio García"

        # Act
        result = person.get_complaint()

        # Assert
        self.assertEqual(expected, result)

    def test_new_agent(self):
        # Arrange
        new_assignment = Agent()
        new_assignment.set_agent(agent)
        expected = {"name": "Roberto Medina", "police_id": "256478",
                    "department": "departmentX"}

        # Act
        result = new_assignment.get_agent()

        # Assert
        self.assertEqual(expected, result)

    def test_new_whistleblower(self):
        # Arrange
        case = Whistleblower()
        case.set_whistleblower(whistleblower)
        expected = {"complaint": "Antonio García", "license": "00001AAA", "color": "rojo",
                    "type": "carretera", "status": "desaparecida", "owner": "Jose García",
                    "date": "19/03/2022", "description": "sin descripción",
                    "address": "c/Francisco de Goya, 3"}

        # Act
        result = case.get_whistleblower()

        # Assert
        self.assertEqual(expected, result)

    # def test_define_bike_from_whistleblower(self):
    #     # Arrange
    #     case = Whistleblower()
    #     case.set_whistleblower(whistleblower)
    #     case.set_bike_instance()
    #     expected = {"license": "00001AAA", "color": "rojo", "type": "carretera",
    #                 "status": "desaparecida", "owner": "Jose García", "date": "19/03/2022",
    #                 "description": "sin descripción", "address": "c/Francisco de Goya, 3"}
    #
    #     # Act
    #     result = case.get_whistleblower()
    #
    #     # Assert
    #     self.assertEqual(expected, result)

    def test_define_complaint_from_whistleblower(self):
        pass

    def test_department_random_assignment(self):
        # Arrange
        department = Department()
        expected = "randomized"

        # Act
        result = department.set_department()
        if result in department._department:
            result = "randomized"

        # Assert
        self.assertEqual(expected, result)

    # def test_unassigned_department(self):
    #     # Arrange
    #     incident = IncidentManager()
    #     # Department().available_department = False
    #     # Department().set_department_availability()
    #     incident.set_bike(bike_description)
    #     expected = "not assigned"
    #
    #     # Act
    #     result = bike.get_department()
    #
    #     # Assert
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
