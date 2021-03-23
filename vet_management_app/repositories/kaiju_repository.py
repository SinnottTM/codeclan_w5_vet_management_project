# Vet repo, got assist by Malcolm, will assume all current code is working fine!
from db.run_sql import run_sql

from models.kaiju import Kaiju

# CRUD

#CREATE
def save_kaiju(kaiju):
    sql = "INSERT INTO kaiju( name, dob, kaiju_type, treatment_notes ) VALUES ( %s, %s, %s, %s ) RETURNING *"
    values = [kaiju.name, kaiju.dob, kaiju.kaiju_type, kaiju.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    kaiju.id = id
    # return kaiju

#READ 
def select_all_kaiju():
    kaiju_list = []

    sql = "SELECT * FROM kaiju"
    results = run_sql(sql)

    for row in results:
        kaiju = Kaiju(row['name'], row['dob'], row['kaiju_type'],
                        row['treatment_notes'], row['id'])
        kaiju_list.append(kaiju)
    return kaiju_list

def select_single_kaiju(id):
    kaiju = None
    sql = "SELECT * FROM kaiju WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        kaiju = Kaiju(result['kaiju.name'], result['kaiju.dob'], result['kaiju.kaiju_type'], result['kaiju.treatment_notes'], result['kaiju.id'])
    return kaiju

#UPDATE
def update(kaiju):
    sql = "UPDATE kaiju SET (name, dob, kaiju_type, treatment_notes) = (%s, %s, %s, %s ) WHERE id = %s"
    values = [kaiju.name, kaiju.dob, kaiju.kaiju_type,
              kaiju.treatment_notes, kaiju.id]
    run_sql(sql, values)

#DELETE
def delete_all_kaiju():
    sql = "DELETE FROM kaiju"
    run_sql(sql)

def delete_single_kaiju(id):
    sql = "DELETE FROM kaiju WHERE id = %s"
    values = [id]
    run_sql(sql, values)
