-- Add primary and foreign keys to tables
-- Alter the data types

-- For tables
--ALTER TABLE countries
--DROP CONSTRAINT countries_pkey;

ALTER TABLE emission_goals 
ADD PRIMARY KEY (country);

ALTER TABLE emissions 
ADD PRIMARY KEY (country);

ALTER TABLE energy_consumption
ADD PRIMARY KEY (country);

ALTER TABLE renewable_energy
ADD PRIMARY KEY (country);

ALTER TABLE nonrenewable_energy
ADD PRIMARY KEY (country);