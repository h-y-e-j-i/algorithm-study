WITH UNION_TABLE AS(
    SELECT
        FLAVOR,
        TOTAL_ORDER
    FROM
        FIRST_HALF

    UNION ALL

    SELECT
        FLAVOR,
        TOTAL_ORDER
    FROM
        JULY
)
SELECT
    FLAVOR
FROM
    UNION_TABLE
GROUP BY
    1
ORDER BY
    SUM(TOTAL_ORDER) DESC
LIMIT 3