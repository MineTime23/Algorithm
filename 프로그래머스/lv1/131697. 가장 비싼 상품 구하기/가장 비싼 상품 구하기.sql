-- 코드를 입력하세요
SELECT PRICE AS MAX_PRICE
FROM (
    SELECT PRICE
    FROM PRODUCT
    ORDER BY PRICE DESC
     )
WHERE ROWNUM = 1