SELECT DISTINCT(CITY) FROM STATION
WHERE SUBSTRING(CITY, 1, 1) IN ('a','e','i','o','u')
and SUBSTRING(CITY, length(CITY), length(CITY)) IN ('a','e','i','o','u');