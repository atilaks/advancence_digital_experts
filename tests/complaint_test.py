import unittest
from code import Complaint


class TestComplaint(unittest.TestCase):
    def setUp(self) -> None:
        self.complaint_description = {"name": "José", "surname": "García", "passport": "56475215f"}
        self.complaint = Complaint(self.complaint_description)

    def test_define_complaint(self):
        # Arrange
        expected = {"name": "José", "surname": "García", "passport": "56475215f"}

        # Act
        full_complaint_description = self.complaint.full_description

        # Assert
        self.assertEqual(expected, full_complaint_description)

    def test_name_modification(self):
        # Arrange
        expected = "José Miguel"
        self.complaint.name = "José Miguel"

        # Act
        new_name = self.complaint.name

        # Assert
        self.assertEqual(expected, new_name)

    def test_surname_modification(self):
        # Arrange
        expected = "Gracia"
        self.complaint.surname = "Gracia"

        # Act
        new_surname = self.complaint.surname

        # Assert
        self.assertEqual(expected, new_surname)

    def test_passport_modification(self):
        # Arrange
        expected = "56475215t"
        self.complaint.passport = "56475215t"

        # Act
        new_passport = self.complaint.passport

        # Assert
        self.assertEqual(expected, new_passport)


if __name__ == '__main__':
    unittest.main()
