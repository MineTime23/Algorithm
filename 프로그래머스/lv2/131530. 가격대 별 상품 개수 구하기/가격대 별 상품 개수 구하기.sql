SELECT PRICE AS "PRICE_GROUPS", COUNT(*) AS "PRODUCTS"
FROM (
    SELECT PRODUCT_CODE, FLOOR(PRICE/10000)*10000 AS "PRICE"
    FROM PRODUCT
    )
GROUP BY PRICE
ORDER BY PRICE