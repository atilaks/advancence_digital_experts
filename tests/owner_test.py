import unittest
from code import Owner, Bike


class TestOwner(unittest.TestCase):
    def setUp(self) -> None:
        self.bike1 = Bike(license_id="00001AAA", color="rojo", bike_type="carretera")
        self.bike2 = Bike(license_id="00301AAA", color="azul", bike_type="carretera")

        bike_dic = {"b1": self.bike1, "b2": self.bike2}

        self.owner = Owner(bike_dic, name="José", surname="García")

    def test_define_owner(self):
        # Arrange
        expected = {"name": "José", "surname": "García", "passport": "sin registro"}

        # Act
        full_owner_description = self.owner.full_description

        # Assert
        self.assertEqual(expected, full_owner_description)

    def test_name_modification(self):
        # Arrange
        expected = "José Miguel"
        self.owner.name = "José Miguel"

        # Act
        new_name = self.owner.name

        # Assert
        self.assertEqual(expected, new_name)

    def test_surname_modification(self):
        # Arrange
        expected = "Gracia"
        self.owner.surname = "Gracia"

        # Act
        new_surname = self.owner.surname

        # Assert
        self.assertEqual(expected, new_surname)

    def test_passport_modification(self):
        # Arrange
        expected = "56475215t"
        self.owner.passport = "56475215t"

        # Act
        new_passport = self.owner.passport

        # Assert
        self.assertEqual(expected, new_passport)

    def test_bike_description(self):
        # Arrange
        expected = "56475215t"
        self.owner.passport = "56475215t"

        # Act
        new_passport = self.owner.passport

        # Assert
        self.assertEqual(expected, new_passport)

    def test_first_bike_of_owner_with_two_bikes(self):
        # Arrange
        expected = {"license_id": "00001AAA", "color": "rojo", "bike_type": "carretera",
                    "description": "sin descripción"}

        # Act
        full_owner_description = self.owner.bike_description("b1")

        # Assert
        self.assertEqual(expected, full_owner_description)

    def test_second_bike_of_owner_with_two_bikes(self):
        # Arrange
        expected = {"license_id": "00301AAA", "color": "azul", "bike_type": "carretera",
                    "description": "sin descripción"}

        # Act
        full_owner_description = self.owner.bike_description("b2")

        # Assert
        self.assertEqual(expected, full_owner_description)


if __name__ == '__main__':
    unittest.main()
