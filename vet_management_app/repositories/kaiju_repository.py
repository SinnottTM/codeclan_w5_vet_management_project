# Kaiju repo, 1st attempt.
from db.run_sql import run_sql

from models.kaiju import Kaiju
import repositories.kaiju_repository as kaiju_repository

# CRUD

#CREATE
def save(kaiju):
    sql = "INSERT INTO kaiju( name, dob, type, owner_id, vet_id, treatment_notes ) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING *"
    values = [kaiju.name, kaiju.dob, kaiju.kaiju_type,
              kaiju.kaiju_owner, kaiju.vet_assigned, kaiju.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    kaiju.id = id
    return kaiju

#READ 
def select_all_kaiju():
    kaiju_list = []

    sql = "SELECT * FROM kaiju"
    results = run_sql(sql)

    for row in results:
        kaiju = Kaiju(row['name'], row['dob'], row['type'], row['owner_id'], row['vet_id'],
                        row['treatment_notes'])
        kaiju_list.append(kaiju)
    return kaiju_list

def select_single_kaiju(id):
    kaiju = None
    sql = "SELECT * FROM kaiju WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        kaiju = Kaiju(kaiju.name, kaiju.dob, kaiju.kaiju_type,
                      kaiju.kaiju_owner, kaiju.vet_assigned, kaiju.treatment_notes)
    return kaiju

#UPDATE
def update(kaiju):
    sql = "UPDATE kaiju SET (name, dob, type, owner_id, vet_id, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [kaiju.name, kaiju.dob, kaiju.kaiju_type,
              kaiju.kaiju_owner, kaiju.vet_assigned, kaiju.treatment_notes]
    run_sql(sql, values)

#DELETE
def delete_all_kaiju():
    sql = "DELETE FROM kaiju"
    run_sql(sql)


def delete_single_kaiju(id):
    sql = "DELETE FROM kaiju WHERE id = %s"
    values = [id]
    run_sql(sql, values)
