# test file for Kaiju, all tests here currently pass
import unittest
from models.kaiju import Kaiju

class TestKaiju(unittest.TestCase):

    def setUp(self):
        self.kaiju = Kaiju("Slattern", "2020", "Category V",
                           "Gypsy Danger's nuclear turbine to the chest")

    def test_kaiju_has_name(self):
        self.assertEqual("Slattern", self.kaiju.name)

    def test_kaiju_has_dob(self):
        self.assertEqual("2020", self.kaiju.dob)

    def test_kaiju_has_kaiju_type(self):
        self.assertEqual("Category V", self.kaiju.kaiju_type)

    def test_kaiju_has_treatment_notes(self):
        self.assertEqual("Gypsy Danger's nuclear turbine to the chest", self.kaiju.treatment_notes)
