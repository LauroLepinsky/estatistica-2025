WITH tb_usuario AS(
    SELECT idUsuario,
        sum(qtdPontos) AS qtdPontos
    FROM points
    GROUP BY idUsuario
),
tb_subset_mediana AS(
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (
            SELECT count(*) % 2 == 0
            FROM tb_usuario
        ) OFFSET (
            SELECT 2 * count(*) / 4
            FROM tb_usuario
        )
),
tb_mediana AS(
    SELECT AVG(qtdPontos) AS mediana
    FROM tb_subset_mediana
),
tb_subset_quartil_01 AS(
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (
            SELECT count(*) % 2 == 0
            FROM tb_usuario
        ) OFFSET (
            SELECT 1 * count(*) / 4
            FROM tb_usuario
        )
),
tb_quartil_01 AS (
    SELECT AVG(qtdPontos) AS quartil_01
    FROM tb_subset_quartil_01
),
tb_subset_quartil_03 AS(
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (
            SELECT count(*) % 2 == 0
            FROM tb_usuario
        ) OFFSET (
            SELECT 3 * count(*) / 4
            FROM tb_usuario
        )
),
tb_quartil_03 AS (
    SELECT AVG(qtdPontos) AS quartil_03
    FROM tb_subset_quartil_03
),
tb_stats AS (
    SELECT min(qtdPontos) AS minimo,
        avg(qtdPontos) AS media,
        max(qtdPontos) AS maximo
    FROM tb_usuario
)
SElECT *
FROM tb_stats,
    tb_mediana,
    tb_quartil_01,
    tb_quartil_03