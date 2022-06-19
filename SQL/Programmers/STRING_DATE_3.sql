-- 중성화 여부 파악하기

-- IF사용
/*
SELECT ANIMAL_ID, NAME, if(SEX_UPON_INTAKE REGEXP ('Neutered|Spayed'), 'O', 'X' ) 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
*/

-- CASE 사용
SELECT ANIMAL_ID, NAME, 
CASE
when SEX_UPON_INTAKE REGEXP('Neutered|Spayed') then 'O'
else 'X'
end 중성화
FROm ANIMAL_INS
ORDER BY ANIMAL_ID;