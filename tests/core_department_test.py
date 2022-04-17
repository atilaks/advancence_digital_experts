import unittest
from code import CoreDepartment, Department


class TestCoreDepartment(unittest.TestCase):
    def setUp(self) -> None:
        self.department = Department(name="DepartamentoA", address="calle Las vacas, 12, Benetússer, 46910")
        self.a_department = {"D1": self.department}

        self.core_department = CoreDepartment(self.a_department)

    def test_how_many_department(self):
        # Arrange
        expected = {"D1": self.department}

        # Act
        available = self.core_department.departments

        # Assert
        self.assertEqual(expected, available)

    def test_new_department(self):
        # Arrange
        department2 = Department(name="DepartamentoB", address="calle Las barcas, 8, Alfafar, 46910")
        expected = {"D1": self.department, "D2": department2}

        # Act
        self.core_department.add_department("D2", department2)
        available = self.core_department.departments

        # Assert
        self.assertEqual(expected, available)

    def test_assign_complaint(self):
        # Arrange
        expected = []

        # Act
        available = self.core_department.department_availability

        # Assert
        self.assertEqual(expected, available)

    def test_none_department_availability(self):
        # Arrange
        expected = []

        # Act
        available = self.core_department.department_availability

        # Assert
        self.assertEqual(expected, available)



    # def test_add_department_availability(self):
    #     # Arrange
    #     department = Department(name="DepartamentoA", address="calle Las barcas, 8, Alfafar, 46910")
    #     expected = [{"name": "DepartamentoA", "address": "calle Las barcas, 8, Alfafar, 46910",
    #                 "agents": None}]
    #
    #     # Act
    #     self.core_department._add_department_to_list("d1", department)
    #     available = self.core_department.department_availability
    #     # Assert
    #     self.assertEqual(expected, available)


if __name__ == '__main__':
    unittest.main()
