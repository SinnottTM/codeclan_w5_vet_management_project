# test file for Kaiju, example case
import unittest
from models.kaiju import Kaiju

class TestKaiju(unittest.TestCase):

    def setUp(self):
        self.kaiju = Kaiju("Slattern", "2020", "Category V", "OWNER ID TO GO HERE", "VET ID TO GO HERE", "Nuke to the Face")

    def test_kaiju_has_name(self):
        self.assertEqual("Slattern", self.kaiju.name)

    def test_kaiju_has_dob(self):
        self.assertEqual("2020", self.kaiju.dob)

    def test_kaiju_has_kaiju_type(self):
        self.assertEqual("Category V", self.kaiju.kaiju_type)

    def test_kaiju_has_kaiju_owner(self):
        self.assertEqual("OWNER ID TO GO HERE", self.kaiju.kaiju_owner)

    def test_kaiju_has_kaiju_vet(self):
        self.assertEqual("VET ID TO GO HERE", self.kaiju.kaiju_vet)

    def test_kaiju_has_treatment_notes(self):
        self.assertEqual("Nuke to the Face", self.kaiju.treatment_notes)