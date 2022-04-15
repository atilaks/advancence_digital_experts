import unittest
from code import Bike


class TestBike(unittest.TestCase):
    def setUp(self) -> None:
        self.bike_description = {"license": "00001AAA", "color": "rojo", "type": "carretera",
                                 "description": "sin descripción"}
        self.bike = Bike(self.bike_description)

    def test_define_bike(self):
        # Arrange
        expected = {"license": "00001AAA", "color": "rojo", "type": "carretera",
                    "description": "sin descripción"}

        # Act
        full_bike_description = self.bike.full_description

        # Assert
        self.assertEqual(expected, full_bike_description)

    def test_license_modification(self):
        # Arrange
        expected = "56782ADF"
        self.bike.license = "56782ADF"

        # Act
        new_license = self.bike.license

        # Assert
        self.assertEqual(expected, new_license)

    def test_color_modification(self):
        # Arrange
        expected = "azul"
        self.bike.color = "azul"

        # Act
        new_color = self.bike.color

        # Assert
        self.assertEqual(expected, new_color)

    def test_type_modification(self):
        # Arrange
        expected = "montaña"
        self.bike.type = "montaña"

        # Act
        new_type = self.bike.type

        # Assert
        self.assertEqual(expected, new_type)

    def test_description_modification(self):
        # Arrange
        expected = "otra descripción"
        self.bike.description = "otra descripción"

        # Act
        new_description = self.bike.description

        # Assert
        self.assertEqual(expected, new_description)


if __name__ == '__main__':
    unittest.main()
