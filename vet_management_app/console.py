# console file, appears to be working fine
import pdb

from models.kaiju import Kaiju
from models.vet import Vet
import repositories.kaiju_repository as kaiju_repository
import repositories.vet_repository as vet_repository

kaiju_repository.delete_all_kaiju()
vet_repository.delete_all_vets()

kaiju_1 = Kaiju("Godzilla", "1954", "Sea Monster",
                 "Oxygen Destroyer")
kaiju_2 = Kaiju("King Kong", "1933", "Eight Wonder of the World",
                "Beauty (what slayed the beast)")
kaiju_3 = Kaiju("Slattern", "2020", "Category V",
                 "Gypsy Danger's nuclear turbine to the chest")
kaiju_4 = Kaiju("Shin_Godzilla", "2016", "Sea Monster",
                "Oral Coagulant Injection")


kaiju_repository.save_kaiju(kaiju_1)
kaiju_repository.save_kaiju(kaiju_2)
kaiju_repository.save_kaiju(kaiju_3)
kaiju_repository.save_kaiju(kaiju_4)

vet_1 = Vet("Dr. Daisuke Serizawa", kaiju_1)
vet_2 = Vet("Carl Denham", kaiju_2)
vet_3 = Vet("Marshal Stacker Pentecost", kaiju_3)

vet_repository.save_vet(vet_1)
vet_repository.save_vet(vet_2)
vet_repository.save_vet(vet_3)

pdb.set_trace()
