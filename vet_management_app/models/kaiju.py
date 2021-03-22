#  Kaiju class, 1st full version
class Kaiju:
    def __init__(self, name, dob, kaiju_type, kaiju_owner, kaiju_vet, treatment_notes):
        self.name = name
        self.dob = dob
        self.kaiju_type = kaiju_type
        self.kaiju_owner = None
        self.kaiju_vet = None
        self.treatment_notes = treatment_notes

    def assign_vet(self, kaiju_vet):
        self.kaiju_vet = kaiju_vet

    def assign_owner(self, kaiju_owner):
        self.kaiju_owner = kaiju_owner
