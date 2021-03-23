# test file for Vet, all tests here currently pass

import unittest
from models.vet import Vet
from models.kaiju import Kaiju

class TestVet(unittest.TestCase):

    
    def setUp(self):
        self.kaiju_1 = Kaiju("Godzilla", "1954", "Sea Monster",
                        "Oxygen Destroyer")
        self.vet = Vet("Dr. Daisuke Serizawa", self.kaiju_1)

    def test_vet_has_name(self):
        self.assertEqual("Dr. Daisuke Serizawa", self.vet.name)

    def test_vet_has_kaiju(self):
        self.assertEqual(self.kaiju_1, self.vet.kaiju)

    def test_vet_kaiju_has_correct_kaiju_name(self):
        self.assertEqual(self.kaiju_1.name, self.vet.kaiju.name)
