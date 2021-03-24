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

-- CREATE TABLE bookings (
--     id SERIAL PRIMARY KEY,
--     monday BOOLEAN,
--     tuesday BOOLEAN,
--     wednesday BOOLEAN,
--     thursday BOOLEAN,
--     friday BOOLEAN,
--     morning BOOLEAN,
--     afternoon BOOLEAN,
--     vet_id INT REFERENCES vets(id) ON DELETE CASCADE
-- );