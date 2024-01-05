SELECT
    YEAR(ONLINE_SALE.SALES_DATE) AS YEAR,
    MONTH(ONLINE_SALE.SALES_DATE)AS MONTH,
    COUNT(DISTINCT ONLINE_SALE.USER_ID) AS PUCHASED_USERS,
    ROUND(COUNT(DISTINCT ONLINE_SALE.USER_ID)/(SELECT COUNT(DISTINCT USER_ID) FROM USER_INFO WHERE YEAR(JOINED)=2021), 1) AS PUCHASED_RATIO
FROM
    USER_INFO
INNER JOIN
    ONLINE_SALE
ON
    USER_INFO.USER_ID=ONLINE_SALE.USER_ID
WHERE
    YEAR(USER_INFO.JOINED)=2021
GROUP BY
    1, 2
ORDER BY
    1, 2
