-- 중복 제거하기
SELECT count(distinct(NAME)) from ANIMAL_INS
WHERE NAME IS NOT NULL;