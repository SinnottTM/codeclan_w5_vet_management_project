class Kaiju:
    def __init__(self, name, dob, kaiju_type, treatment_notes, vet, registered = False, id = None):
        self.id = id
        self.name = name
        self.dob = dob
        self.kaiju_type = kaiju_type
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.registered = registered
