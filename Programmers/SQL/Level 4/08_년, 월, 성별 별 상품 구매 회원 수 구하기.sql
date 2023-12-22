SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH, U.GENDER, COUNT(DISTINCT O.USER_ID) AS USERS
FROM USER_INFO U, ONLINE_SALE O
WHERE U.USER_ID = O.USER_ID AND U.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, U.GENDER
ORDER BY YEAR, MONTH, U.GENDER;