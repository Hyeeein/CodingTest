SELECT G.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E,
    (SELECT EMP_NO, SUM(SCORE) AS SCORE
     FROM HR_GRADE
     WHERE YEAR = 2022
     GROUP BY EMP_NO
     ORDER BY SCORE DESC
     LIMIT 1) G
WHERE E.EMP_NO = G.EMP_NO