import unittest
from code import Department
# from . import Agent


class TestDepartment(unittest.TestCase):
    def setUp(self) -> None:
        # self.agent1 = Agent(name="José", surname="García", passport="56475215f", police_id="A5826",
        #                    department="departmentA", range="official")
        # self.agent2 = Agent(name="Julio", surname="Montero", passport="56564715f", police_id="D5876",
        #                    department="departmentA", range="comisario")
        #
        # agents = {"a1": self.agent1, "a2": self.agent2}

        self.department = Department(name="DepartamentoA", address="calle Colón, 12, Massanassa, 46470")

    def test_define_department(self):
        # Arrange
        expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
                    "agents": {}}

        # expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
        #             "agents": {{"name": "José", "surname": "García", "passport": "56475215f",
        #                         "police_id": "A5826", "department": "departmentA", "range": "official"},
        #                        {"name": "Julio", "surname": "Montero", "passport": "56564715f",
        #                         "police_id": "D5876", "department": "departmentA", "range": "comisario"}}}

        # Act
        full_department_description = self.department.full_description

        # Assert
        self.assertEqual(expected, full_department_description)

    def test_name_modification(self):
        # Arrange
        expected = "DepartamentoB"
        self.department.name = "DepartamentoB"

        # Act
        new_name = self.department.name

        # Assert
        self.assertEqual(expected, new_name)

    def test_address_modification(self):
        # Arrange
        expected = "calle Blasco Ibáñez, 3, Catarroja, 46470"
        self.department.address = "calle Blasco Ibáñez, 3, Catarroja, 46470"

        # Act
        new_address = self.department.address

        # Assert
        self.assertEqual(expected, new_address)

    # def test_add_agents(self):
    #     # Arrange
    #     expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
    #                 "agents": {{"name": "José", "surname": "García", "passport": "56475215f",
    #                             "police_id": "A5826", "department": "departmentA", "range": "official"},
    #                            {"name": "Julio", "surname": "Montero", "passport": "56564715f",
    #                             "police_id": "D5876", "department": "departmentA", "range": "comisario"},
    #                            {"name": "Pepe", "surname": "Otero", "passport": "87946215s",
    #                             "police_id": "R8626", "department": "departmentA", "range": "official"}}}
    #
    #     self.agent3 = Agent(name="Pepe", surname="Otero", passport="87946215s", police_id="R8626",
    #                         department="departmentA", range="official")
    #
    #     # Act
    #     add_agent = self.department.agents(self.agent3)
    #
    #     # Assert
    #     self.assertEqual(expected, add_agent)
    #
    # def test_drop_agents(self):
    #     # Arrange
    #     expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
    #                 "agents": {{"name": "José", "surname": "García", "passport": "56475215f",
    #                             "police_id": "A5826", "department": "departmentA", "range": "official"}}}
    #     self.agent = "D5876"
    #
    #     # Act
    #     drop_agent = self.department.agents(self.agent)
    #
    #     # Assert
    #     self.assertEqual(expected, drop_agent)


if __name__ == '__main__':
    unittest.main()
