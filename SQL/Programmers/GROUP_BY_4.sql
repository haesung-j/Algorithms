-- 입양 시각 구하기(2)
SET @h := -1;

SELECT (@h := @h + 1),
(SELECT count(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @h)
FROM ANIMAL_OUTS
WHERE @h <23;