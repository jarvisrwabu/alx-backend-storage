-- Use CASE to get the lifespan of band
SELECT DISTINCT(band_name),
CASE
    WHEN split IS NULL THEN 2022 - formed
    ELSE split - formed
END AS lifespan
FROM metal_bands
ORDER BY lifespan DESC;