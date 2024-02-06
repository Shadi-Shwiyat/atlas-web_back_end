-- Script ranks country origins of bands,
-- ordered by the number of (non-unique) fans

DROP TABLE IF EXISTS tmp_res;
CREATE TABLE IF NOT EXISTS tmp_res (
    origin varchar(255),
    nb_fans INT
);

INSERT INTO tmp_res (origin, nb_fans)
SELECT origin, SUM(fans) as total_fans
FROM metal_bands
GROUP BY origin;

SELECT *
FROM tmp_res
ORDER BY nb_fans DESC;