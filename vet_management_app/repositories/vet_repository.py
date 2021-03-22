# Vet repo, 1st attempt.
from db.run_sql import run_sql

from models.vet import Vet
import repositories.vet_repository as vet_repository

# CRUD

#CREATE
def save(vet):
    sql = "INSERT INTO vet( name, kaiju_id, owner_id ) VALUES ( %s, %s, %s) RETURNING *"
    values = [vet.name, vet.kaiju_id, vet.owner_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

#READ
def select_all_vets():
    vet_list = []

    sql = "SELECT * FROM vet"
    results = run_sql(sql)

    for row in results:
        vet = vet(row['name'], row['kaiju_id'], row['owner_id'])
        vet_list.append(vet)
    return vet_list

def select_single_vet(id):
    vet = None
    sql = "SELECT * FROM vet WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(vet.name, vet.kaiju_id, vet.owner_id)
    return vet

#UPDATE
def update(vet):
    sql = "UPDATE vet SET ( name, kaiju_id, owner_id ) = (%s, %s, %s) WHERE id = %s"
    values = [vet.name, vet.kaiju_id, vet.owner_id]
    run_sql(sql, values)

#DELETE
def delete_all_vets():
    sql = "DELETE FROM kaiju"
    run_sql(sql)


def delete_single_vet(id):
    sql = "DELETE FROM vet WHERE id = %s"
    values = [id]
    run_sql(sql, values)
