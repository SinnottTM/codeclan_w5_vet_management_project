--  Vet repo, got assist by Malcolm, will assume all current code is working fine!
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS kaiju;

CREATE TABLE kaiju ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    kaiju_type VARCHAR(255),
    treatment_notes TEXT
);

CREATE TABLE vets ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    kaiju_id INT REFERENCES kaiju(id) ON DELETE CASCADE
);
