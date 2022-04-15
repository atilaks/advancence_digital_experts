import unittest
from code import DepartmentManager


class TestAgent(unittest.TestCase):
    def setUp(self) -> None:
        self.department_manager_description = {"name": "José", "surname": "García", "passport": "56475215f",
                                               "police id": "A5826", "department": "departmentA",
                                               "range": "commissar"}
        self.department_manager = DepartmentManager(self.department_manager_description)

    def test_define_agent(self):
        # Arrange
        expected = {"name": "José", "surname": "García", "passport": "56475215f",
                    "police id": "A5826", "department": "departmentA", "range": "commissar"}

        # Act
        person_description = self.department_manager.all_features

        # Assert
        self.assertEqual(expected, person_description)

    def test_name_modification(self):
        # Arrange
        expected = "José Miguel"
        self.department_manager.name = "José Miguel"

        # Act
        new_name = self.department_manager.name

        # Assert
        self.assertEqual(expected, new_name)

    def test_surname_modification(self):
        # Arrange
        expected = "Gracia"
        self.department_manager.surname = "Gracia"

        # Act
        new_surname = self.department_manager.surname

        # Assert
        self.assertEqual(expected, new_surname)

    def test_passport_modification(self):
        # Arrange
        expected = "56475215t"
        self.department_manager.passport = "56475215t"

        # Act
        new_passport = self.department_manager.passport

        # Assert
        self.assertEqual(expected, new_passport)

    def test_police_id_modification(self):
        # Arrange
        expected = "A5827"
        self.department_manager.police_id = "A5827"

        # Act
        new_police_id = self.department_manager.police_id

        # Assert
        self.assertEqual(expected, new_police_id)

    def test_department_modification(self):
        # Arrange
        expected = "departmentB"
        self.department_manager.department = "departmentB"

        # Act
        new_department = self.department_manager.department

        # Assert
        self.assertEqual(expected, new_department)

    def test_manager_modification(self):
        # Arrange
        expected = "commissar"
        self.department_manager.manager = "commissar"

        # Act
        new_department = self.department_manager.manager

        # Assert
        self.assertEqual(expected, new_department)


if __name__ == '__main__':
    unittest.main()
