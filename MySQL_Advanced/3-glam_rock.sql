-- lists all bands with Glam rock as their main style,
-- ranked by their longevity

DROP TABLE IF EXISTS tmp_res;
CREATE TABLE IF NOT EXISTS tmp_res (
    band_name varchar(255),
    lifespan INT
);

INSERT INTO tmp_res (band_name, lifespan)
SELECT band_name, (IFNULL(split, 2020)) - formed as difference
FROM metal_bands
WHERE style LIKE '%Glam rock%';

SELECT *
FROM tmp_res
ORDER BY lifespan DESC, band_name DESC;