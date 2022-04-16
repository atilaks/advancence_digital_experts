import unittest
from code import CoreDepartment


class TestCoreDepartment(unittest.TestCase):
    def setUp(self) -> None:
        self.bike = CoreDepartment(license_id="00001AAA", color="rojo", bike_type="carretera")

    def test_define_bike(self):
        # Arrange
        expected = {"license_id": "00001AAA", "color": "rojo", "bike_type": "carretera",
                    "description": "sin descripción"}

        # Act
        full_bike_description = self.bike.full_description

        # Assert
        self.assertEqual(expected, full_bike_description)


if __name__ == '__main__':
    unittest.main()
