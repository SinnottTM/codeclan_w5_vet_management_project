# Vet repo, got assist by Malcolm, will assume all current code is working fine!
from db.run_sql import run_sql

from models.vet import Vet
from models.kaiju import Kaiju
import repositories.kaiju_repository as kaiju_repository

# CRUD

#CREATE
def save_vet(vet):
    sql = "INSERT INTO vets( name, kaiju_id ) VALUES ( %s, %s ) RETURNING *"
    values = [vet.name, vet.kaiju.id]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    # return vet

#READ
def select_all_vets():
    vet_list = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        kaiju = kaiju_repository.select_single_kaiju(row["kaiju_id"])
        vet = Vet(row['name'], kaiju, row['id'])
        vet_list.append(vet)
    return vet_list

def select_single_vet(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        kaiju = kaiju_repository.select_single_kaiju(result["kaiju_id"])
        vet = Vet(result['name'], kaiju, result['id'])
    return vet

#UPDATE
def update_vet(vet):
    sql = "UPDATE vets SET ( name, kaiju_id ) = ( %s, %s ) WHERE id = %s"
    values = [vet.name, vet.kaiju.id, vet.id]
    run_sql(sql, values)

#DELETE
def delete_all_vets():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete_single_vet(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)
