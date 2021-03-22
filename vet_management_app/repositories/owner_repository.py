# Vet repo, 1st attempt.
from db.run_sql import run_sql

from models.owner import Owner
import repositories.owner_repository as owner_repository

# CRUD

#CREATE
def save(owner):
    sql = "INSERT INTO owners( name ) VALUES ( %s ) RETURNING *"
    values = [owner.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

#READ
def select_all_owners():
    owner_list = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['name'])
        owner_list.append(owner)
    return owner_list

def select_single_owner(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(owner.name)
    return owner

#UPDATE
def update(owner):
    sql = "UPDATE owners SET ( name ) = ( %s ) WHERE id = %s"
    values = [owner.name]
    run_sql(sql, values)

#DELETE
def delete_all_owners():
    sql = "DELETE FROM owners"
    run_sql(sql)


def delete_single_owner(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)
