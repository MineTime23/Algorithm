SELECT ROUND(SUM(DAILY_FEE) / COUNT(*),0) AS AVERAGE_FEE
FROM (
    SELECT CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE = 'SUV'
    ) AS SubqueryAlias;
