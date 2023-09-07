SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE BETWEEN 20 AND 29 
    AND EXTRACT(YEAR FROM JOINED) = 2021