import unittest
from models.vet import Vet
from models.kaiju import Kaiju

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet = Vet("Dr. Daisuke Serizawa")
        self.kaiju_1 = Kaiju("Godzilla", "1954", "Sea monster",
                        "Oxygen Destroyer", self.vet, True)
        self.kaiju_2 = Kaiju("Shin_Godzilla", "2016", "Sea monster",
                "Oral coagulant injection (10000 litres plus)", self.vet, True)

    def test_vet_has_name(self):
        self.assertEqual("Dr. Daisuke Serizawa", self.vet.name)

    def test_many_kaiju_to_one_vet(self):
        self.assertEqual(self.vet, self.kaiju_1.vet and self.kaiju_2.vet)

        