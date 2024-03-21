-- lists all bands with Glam rock as their main style
SELECT band_name,
       (CASE
            WHEN split IS NOT NULL THEN (2022 - formed)
            ELSE (2022 - formed)
        END) AS lifespan
FROM metal_bands WHERE main_style = 'Glam rock' ORDER BY lifespan DESC;