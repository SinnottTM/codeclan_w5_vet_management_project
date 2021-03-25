import unittest
from models.kaiju import Kaiju
from models.vet import Vet

class TestKaiju(unittest.TestCase):

    def setUp(self):
        self.vet = Vet("Tim Sinnott")
        self.kaiju_1 = Kaiju("Biollante", "1989", "Genetically-modified Rose/Crocodile/Ghost of a death girl kaiju hybrid", "Finding peace while simultaneously exploding", self.vet, True)
        self.kaiju_2 = Kaiju("Destoroyah", "1995", "Sea monster",
                             "Godzilla in meltdown mode", self.vet, False)

    def test_kaiju_has_name(self):
        self.assertEqual("Biollante", self.kaiju_1.name)

    def test_kaiju_has_dob(self):
        self.assertEqual("1989", self.kaiju_1.dob)

    def test_kaiju_has_kaiju_type(self):
        self.assertEqual("Genetically-modified Rose/Crocodile/Ghost of a death girl kaiju hybrid", self.kaiju_1.kaiju_type)

    def test_kaiju_has_treatment_notes(self):
        self.assertEqual("Finding peace while simultaneously exploding", self.kaiju_1.treatment_notes)

    def test_kaiju_has_vet(self):
        self.assertEqual(self.kaiju_1.vet, self.vet)

    def test_kaiju_is_registered(self):
        self.assertEqual(self.kaiju_1.registered, True)

    def test_kaiju_is_not_registered(self):
        self.assertEqual(self.kaiju_2.registered, False)

    def test_one_vet_to_many_kaiju(self):
        self.assertEqual(self.kaiju_1.vet and self.kaiju_2.vet, self.vet)
