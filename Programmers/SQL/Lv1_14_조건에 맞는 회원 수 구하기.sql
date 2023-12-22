SELECT COUNT(AGE) AS USERS
FROM USER_INFO
WHERE (DATE(JOINED) BETWEEN '2021-01-01' AND '2021-12-31') AND (AGE >= 20 AND AGE <= 29);