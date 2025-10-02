WITH tb_freq_abs AS (
    SELECT descCategoriaProduto,
        count(idTransacao) AS FreqAbs
    FROM points
    GROUP BY descCategoriaProduto
),
tb_freq_abs_acum AS (
    SELECT *,
        sum(FreqAbs) OVER(
            PARTITION BY 1
            ORDER BY descCategoriaProduto
        ) AS FreqAbsAcum,
        1.0 * FreqAbs / (
            SELECT sum(FreqAbs)
            FROM tb_freq_abs
        ) AS FreqRel
    FROM tb_freq_abs
)
SELECT *,
    sum(FreqRel) OVER (
        ORDER BY descCategoriaProduto
    ) AS FreqRelAcum
FROM tb_freq_abs_acum