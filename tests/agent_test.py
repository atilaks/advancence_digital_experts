import unittest
from code import Agent


class TestAgent(unittest.TestCase):
    def setUp(self) -> None:
        self.agent_description = {"name": "José", "surname": "García", "passport": "56475215f",
                                  "police id": "A5826", "department": "departmentA",
                                  "range": "official"}
        self.agent = Agent(self.agent_description)

    def test_agent_description(self):
        # Arrange
        expected = {"police id": "A5826", "department": "departmentA", "range": "official"}

        # Act
        only_agent_description = self.agent.agent_description

        # Assert
        self.assertEqual(expected, only_agent_description)

    def test_person_description(self):
        # Arrange
        expected = {"name": "José", "surname": "García", "passport": "56475215f"}

        # Act
        only_person_description = self.agent.full_description

        # Assert
        self.assertEqual(expected, only_person_description)

    def test_define_agent(self):
        # Arrange
        expected = {"name": "José", "surname": "García", "passport": "56475215f",
                    "police id": "A5826", "department": "departmentA", "range": "official"}

        # Act
        person_description = self.agent.all_features

        # Assert
        self.assertEqual(expected, person_description)

    def test_name_modification(self):
        # Arrange
        expected = "José Miguel"
        self.agent.name = "José Miguel"

        # Act
        new_name = self.agent.name

        # Assert
        self.assertEqual(expected, new_name)

    def test_surname_modification(self):
        # Arrange
        expected = "Gracia"
        self.agent.surname = "Gracia"

        # Act
        new_surname = self.agent.surname

        # Assert
        self.assertEqual(expected, new_surname)

    def test_passport_modification(self):
        # Arrange
        expected = "56475215t"
        self.agent.passport = "56475215t"

        # Act
        new_passport = self.agent.passport

        # Assert
        self.assertEqual(expected, new_passport)

    def test_police_id_modification(self):
        # Arrange
        expected = "A5827"
        self.agent.police_id = "A5827"

        # Act
        new_police_id = self.agent.police_id

        # Assert
        self.assertEqual(expected, new_police_id)


if __name__ == '__main__':
    unittest.main()
