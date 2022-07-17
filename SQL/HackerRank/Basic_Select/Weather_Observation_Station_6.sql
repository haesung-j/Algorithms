select distinct(CITY) from STATION
WHERE LOWER(SUBSTRING(CITY, 1, 1)) in ('a','e','i','o','u');