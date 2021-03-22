# console file, TBC
import pdb

from models.kaiju import Kaiju
from models.owner import Owner
from models.vet import Vet
import repositories.kaiju_repository as kaiju_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository


kaiju_repository.delete_all_kaiju()
owner_repository.delete_all_owners()
vet_repository.delete_all_vets()

kaiju_1 = Kaiju("Godzilla", "1954", "Sea Monster",
                "OWNER ID TO GO HERE", "VET ID TO GO HERE", "Oxygen Destroyer")
kaiju_2 = Kaiju("King Kong", "1933", "Eight Wonder of the World",
                "OWNER ID TO GO HERE", "VET ID TO GO HERE", "Nuke to the Face")
kaiju_3 = Kaiju("Slattern", "2020", "Category V",
                "OWNER ID TO GO HERE", "VET ID TO GO HERE", "Nuke to the Face")

owner_1 = Owner("Unregulated Nuclear Testing")
owner_2 = Owner("Whatever foods are available on Skull Island")
owner_3 = Owner("The Precursors")

vet_1 = Vet("Dr. Daisuke Serizawa", "KAIJU ID TO GO HERE")
vet_2 = Vet("Carl Denham", "KAIJU ID TO GO HERE")
vet_3 = Vet("Marshal Stacker Pentecost", "KAIJU ID TO GO HERE")


# Note: assign vet & owner to kaiju before running console.py

owner_repository.save(owner_1)
owner_repository.save(owner_2)
owner_repository.save(owner_3)

vet_repository.save(vet_1)
vet_repository.save(vet_2)
vet_repository.save(vet_3)

kaiju_1.assign_owner(owner_1)
kaiju_2.assign_owner(owner_2)
kaiju_3.assign_owner(owner_3)

kaiju_1.assign_vet(vet_1)
kaiju_2.assign_vet(vet_2)
kaiju_3.assign_vet(vet_3)

kaiju_repository.save(kaiju_1)
kaiju_repository.save(kaiju_2)
kaiju_repository.save(kaiju_3)
