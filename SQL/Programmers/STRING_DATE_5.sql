-- DATETIME에서 DATE로 형 변환

SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') 날짜 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;