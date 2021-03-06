-- WHERE문 사용
/* 
 SELECT NAME, DATETIME FROM ANIMAL_INS as AI
# WHERE AI.ANIMAL_ID not in (select ANIMAL_ID FROM ANIMAL_OUTS)
# ORDER BY DATETIME
# LIMIT 3;
*/

-- JOIN문 사용
SELECT AI.NAME, AI.DATETIME FROM ANIMAL_INS as AI
LEFT JOIN ANIMAL_OUTS as AO
on AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AO.ANIMAL_ID IS NULL
ORDER BY AI.DATETIME
LIMIT 3;