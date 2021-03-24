DROP TABLE IF EXISTS kaiju;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE kaiju ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    kaiju_type VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    registered BOOLEAN
);
