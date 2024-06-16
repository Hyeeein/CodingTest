SELECT E.ID
FROM -- 3세대
     ECOLI_DATA E, -- 2세대
                   (SELECT E.ID 
                    FROM ECOLI_DATA E,
                         -- 1세대
                         (SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IS NULL) G1
                    WHERE E.PARENT_ID = G1.ID) G2
WHERE E.PARENT_ID = G2.ID
ORDER BY E.ID ASC;