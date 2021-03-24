#  Kaiju class, working fine
class Kaiju:
    def __init__(self, name, dob, kaiju_type, treatment_notes, vet_id, id = None):
        self.id = id
        self.name = name
        self.dob = dob
        self.kaiju_type = kaiju_type
        self.treatment_notes = treatment_notes
        self.vet_id = vet_id
