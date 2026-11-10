SELECT species, sex, body_mass_g
FROM penguins
WHERE year == 2007 AND sex IS NOT NULL;
