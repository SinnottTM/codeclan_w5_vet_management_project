# pet_repo, TBC
# from db.run_sql import run_sql

# from models.pet import Pet
# import repositories.pet_repository as pet_repository

# #CREATE
# def save([pet]):
#     sql = "INSERT INTO pets( name, parameter_2, parameter_3, parameter_4 ) VALUES ( %s, %s, %s, %s) RETURNING *"
#     values = [pet.name, pet.parameter_2, pet.parameter_3, pet.parameter_4]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     pet.id = id
#     return pet
