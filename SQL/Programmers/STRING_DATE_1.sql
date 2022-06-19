-- 루시와 엘라 찾기

-- IN 사용
/*
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty');
*/

-- 정규식 사용
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
WHERE NAME REGEXP ('^(LUCY|Ella|Pickle|Rogan|Sabrina|Mitty)$')