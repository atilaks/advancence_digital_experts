import unittest
from code import Complaint, Bike, Owner


class TestComplaint(unittest.TestCase):
    def setUp(self) -> None:
        self.bike = Bike(license_id="00001AAA", color="rojo", bike_type="carretera")
        a_bike = {"b1": self.bike}

        owner = Owner(a_bike, name="José", surname="García")

        self.complaint = Complaint(owner, date="15/03/2022", address="calle Las barcas, 8, Alfafar, 46910",
                                   id_complaint=0)

    def test_define_complaint(self):
        # Arrange
        expected = {'owner': {'name': 'José', 'passport': 'sin registro', 'surname': 'García'},
                    "bike": {"license_id": "00001AAA", "color": "rojo", "bike_type": "carretera",
                             "description": "sin descripción"}, "date": "15/03/2022",
                    "address": "calle Las barcas, 8, Alfafar, 46910", "description": "sin descripción",
                    "status": "desaparecida", "id_complaint": 0}

        full_complaint_description = self.complaint.full_description

        # Assert
        self.assertEqual(expected, full_complaint_description)

    def test_date_modification(self):
        # Arrange
        expected = "16/03/2022"
        self.complaint.date = "16/03/2022"

        # Act
        new_date = self.complaint.date

        # Assert
        self.assertEqual(expected, new_date)

    def test_address_modification(self):
        # Arrange
        expected = "calle Las barcas, 3, Alfafar, 46910"
        self.complaint.address = "calle Las barcas, 3, Alfafar, 46910"

        # Act
        new_date = self.complaint.address

        # Assert
        self.assertEqual(expected, new_date)

    def test_description_modification(self):
        # Arrange
        expected = "oxidada"
        self.complaint.description = "oxidada"

        # Act
        new_date = self.complaint.description

        # Assert
        self.assertEqual(expected, new_date)

    def test_status_modification(self):
        # Arrange
        expected = "encontrada"
        self.complaint.status = "encontrada"

        # Act
        new_date = self.complaint.status

        # Assert
        self.assertEqual(expected, new_date)

    def test_bike_reported(self):
        # Arrange
        expected = {"license_id": "00001AAA", "color": "rojo", "bike_type": "carretera",
                    "description": "sin descripción"}

        # Act
        bike = self.complaint.bike

        # Assert
        self.assertEqual(expected, bike)

    def test_api_geocode(self):
        # Arrange
        expected = {"lat": 39.4700312, "lng": -0.3743573}

        # Act
        address_stole = self.complaint.get_coordinates()

        # Assert
        self.assertAlmostEqual(expected, address_stole)


if __name__ == '__main__':
    unittest.main()
