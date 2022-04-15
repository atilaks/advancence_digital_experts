import unittest
from code.person.individual import Individual


class TestIndividual(unittest.TestCase):
    def setUp(self) -> None:
        self.individual_description = {"name": "José", "surname": "García", "passport": "56475215f"}
        self.individual = Individual(self.individual_description)

    def test_define_individual(self):
        # Arrange
        expected = {"name": "José", "surname": "García", "passport": "56475215f"}

        # Act
        full_individual_description = self.individual.full_description

        # Assert
        self.assertEqual(expected, full_individual_description)

    def test_name_modification(self):
        # Arrange
        expected = "José Miguel"
        self.individual.name = "José Miguel"

        # Act
        new_name = self.individual.name

        # Assert
        self.assertEqual(expected, new_name)

    def test_surname_modification(self):
        # Arrange
        expected = "Gracia"
        self.individual.surname = "Gracia"

        # Act
        new_surname = self.individual.surname

        # Assert
        self.assertEqual(expected, new_surname)

    def test_passport_modification(self):
        # Arrange
        expected = "56475215t"
        self.individual.passport = "56475215t"

        # Act
        new_passport = self.individual.passport

        # Assert
        self.assertEqual(expected, new_passport)


if __name__ == '__main__':
    unittest.main()
