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
vet_4 = Vet("Shin Sang-ok")
vet_5 = Vet("Tim Sinnott")

vet_repository.save_vet(vet_1)
vet_repository.save_vet(vet_2)
vet_repository.save_vet(vet_3)
vet_repository.save_vet(vet_4)
vet_repository.save_vet(vet_5)

kaiju_1 = Kaiju("Godzilla", "1954", "Sea monster", "Oxygen Destroyer", vet_1, True)
kaiju_2 = Kaiju("King Kong", "1933", "Eight Wonder of the World", "Beauty (what slayed the beast)", vet_2, True)
kaiju_3 = Kaiju("Slattern", "2020", "Category V", "Striker Eureka going critical", vet_3, True)
kaiju_4 = Kaiju("Shin_Godzilla", "2016", "Sea monster", "Oral coagulant injection (10000 litres plus)", vet_1, True)
kaiju_5 = Kaiju("Grabbers", "2012", "Sea monster", "Guinness", vet_2, True)
kaiju_6 = Kaiju("Pulgasari", "1985", "Benign and gracious communist savior", "North Korean propaganda", vet_4, True)
kaiju_7 = Kaiju("King Ghidorah", "1964", "Extraterrestrial planet-killing dragon", "Friendly chat with Godzilla", vet_1, True)
kaiju_8 = Kaiju("Biollante", "1989", "Genetically-modified Rose/Crocodile/Ghost of a death girl kaiju hybrid",
                "Finding peace while simultaneously exploding", vet_5, True)
kaiju_9 = Kaiju("Onibaba", "2016", "Category II", "Drop most of Tokyo on it", vet_3, True)
kaiju_10 = Kaiju("Destoroyah", "1995", "Sea monster", "Godzilla in meltdown mode", vet_5, True)

kaiju_repository.save_kaiju(kaiju_1)
kaiju_repository.save_kaiju(kaiju_2)
kaiju_repository.save_kaiju(kaiju_3)
kaiju_repository.save_kaiju(kaiju_4)
kaiju_repository.save_kaiju(kaiju_5)
kaiju_repository.save_kaiju(kaiju_6)
kaiju_repository.save_kaiju(kaiju_7)
kaiju_repository.save_kaiju(kaiju_8)
kaiju_repository.save_kaiju(kaiju_9)
kaiju_repository.save_kaiju(kaiju_10)

pdb.set_trace()