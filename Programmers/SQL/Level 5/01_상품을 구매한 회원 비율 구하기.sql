SELECT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH,
       COUNT(DISTINCT I.USER_ID) AS PUCHASED_USERS,
       ROUND(COUNT(DISTINCT I.USER_ID) / (SELECT COUNT(*) 
                                          FROM USER_INFO 
                                          WHERE YEAR(JOINED)='2021'), 1) AS PUCHASED_RATIO
FROM USER_INFO I, ONLINE_SALE S
WHERE I.USER_ID = S.USER_ID AND YEAR(I.JOINED) = '2021'
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;