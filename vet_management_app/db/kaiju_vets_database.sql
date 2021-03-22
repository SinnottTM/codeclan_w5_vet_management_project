-- Database SQL page
-- Note: May need to reorder drops for referencing etc?
DROP TABLE IF EXISTS kaiju;
DROP TABLE IF EXISTS vets;
DROP TABLE If EXISTS owner;

CREATE TABLE vets ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    kaiju_id INT REFERENCES kaiju(id) ON DELETE CASCADE, 
    owner_id INT REFERENCES owner(id) ON DELETE CASCADE

);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);

CREATE TABLE kaiju ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    owner VARCHAR(255),
    vet_id INT REFERENCES vet(id) ON DELETE CASCADE,
    treatment_notes TEXT

);