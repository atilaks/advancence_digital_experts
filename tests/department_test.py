import unittest
from code import Department
from code import Agent
from code import Complaint


class TestDepartment(unittest.TestCase):
    def setUp(self) -> None:
        self.agent1 = Agent(name="José", surname="García", passport="56475215f", police_id="A5826",
                            department="departmentA", range="official")
        self.agent2 = Agent(name="Julio", surname="Montero", passport="56564715f", police_id="D5876",
                            department="departmentA", range="comisario")

        agents = {"a1": self.agent1, "a2": self.agent2}

        self.department = Department(name="DepartamentoA", address="calle Colón, 12, Massanassa, 46470",
                                     agents=agents)

    def test_define_department(self):
        expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
                    "agents": {"a1": self.agent1, "a2": self.agent2}}

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

    def test_add_agents(self):
        # Arrange
        agent3 = Agent(name="Pepe", surname="Otero", passport="87946215s", police_id="R8626",
                            department="departmentA", range="official")

        expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
                    "agents": {"a1": self.agent1, "a2": self.agent2, "a3": agent3}}

        # Act
        self.department.assign_agent("a3", agent3)
        add_agent = self.department.full_description

        # Assert
        self.assertEqual(expected, add_agent)

    def test_drop_agents(self):
        # Arrange
        expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
                    "agents": {"a1": self.agent1}}
        agent = "D5876"

        # Act
        self.department.remove_agent_by_police_id(agent)
        update_department = self.department.full_description

        # Assert
        self.assertEqual(expected, update_department)

    def test_assign(self):
        # Arrange
        expected = {"name": "DepartamentoA", "address": "calle Colón, 12, Massanassa, 46470",
                    "agents": {"a1": self.agent1}}
        id_complaint = 0
        complaint = Complaint(date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910",
                                   id_complaint=id_complaint)

        # Act
        self.department.assign_complaint(complaint)
        assigned_agents = self.department.assigned_agents(id_complaint)
        not_assigned_agents = self.department.not_assigned_agent()
        close_complaint = self.department.close_complaint(id_complaint)

        # assigned_complaint = self.department.assigned_complaint(police_id)

        # TODO: HACER TRES O CUATRO TEST DE ESTE

        # Assert
        self.assertEqual(expected, update_department)


if __name__ == '__main__':
    unittest.main()
