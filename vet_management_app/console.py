# console file, appears to be working fine
import pdb

from models.kaiju import Kaiju
from models.vet import Vet
import repositories.kaiju_repository as kaiju_repository
import repositories.vet_repository as vet_repository

kaiju_repository.delete_all_kaiju()
vet_repository.delete_all_vets()

vet_1 = Vet("Dr. Daisuke Serizawa")
vet_2 = Vet("Carl Denham")
vet_3 = Vet("Marshal Stacker Pentecost")

vet_repository.save_vet(vet_1)
vet_repository.save_vet(vet_2)
vet_repository.save_vet(vet_3)

kaiju_1 = Kaiju("Godzilla", "1954", "Sea Monster",
                 "Oxygen Destroyer", vet_1)
kaiju_2 = Kaiju("King Kong", "1933", "Eight Wonder of the World",
                "Beauty (what slayed the beast)", vet_2)
kaiju_3 = Kaiju("Slattern", "2020", "Category V",
                 "Gypsy Danger's nuclear turbine to the chest", vet_3)
kaiju_4 = Kaiju("Shin_Godzilla", "2016", "Sea Monster",
                "Oral Coagulant Injection", vet_1)

kaiju_repository.save_kaiju(kaiju_1)
kaiju_repository.save_kaiju(kaiju_2)
kaiju_repository.save_kaiju(kaiju_3)
kaiju_repository.save_kaiju(kaiju_4)

pdb.set_trace()
