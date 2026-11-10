SELECT species, sex, body_mass_g
FROM penguins
WHERE year == 2009 AND sex IS NOT NULL;
