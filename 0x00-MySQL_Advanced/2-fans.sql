-- ranks country by origins of bands ordered by number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands GROUP BY origin ORDER BY SUM(fans) DESC;
