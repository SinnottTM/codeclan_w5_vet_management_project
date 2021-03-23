# Vet repo, 1st attempt.
from db.run_sql import run_sql

from models.vet import Vet
import repositories.vet_repository as vet_repository

# CRUD

#CREATE
def save(vet):
    sql = "INSERT INTO vets( name, kaiju_id ) VALUES ( %s, %s ) RETURNING *"
    values = [vet.name, vet.kaiju_id]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet

#READ
def select_all_vets():
    vet_list = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'], row['kaiju_id'])
        vet_list.append(vet)
    return vet_list

def select_single_vet(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(vet.name, vet.kaiju_id, vet.owner_id)
    return vet

#UPDATE
def update(vet):
    sql = "UPDATE vets SET ( name, kaiju_id ) = ( %s, %s ) WHERE id = %s"
    values = [vet.name, vet.kaiju_id]
    run_sql(sql, values)

#DELETE
def delete_all_vets():
    sql = "DELETE FROM vets"
    run_sql(sql)


def delete_single_vet(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)
