-- SELECT CITY FROM STATION
-- WHERE CITY REGEXP('[^aeiou]$');

SELECT distinct(CITY) FROM STATION
WHERE lower(substring(CITY, length(CITY), length(CITY))) not in ('a', 'e','i','o','u');