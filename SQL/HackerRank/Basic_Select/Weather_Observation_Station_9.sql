-- select distinct(CITY) FROM STATION
-- where lower(CITY) REGEXP ('^[^aeiou]');


select distinct(CITY) FROM STATION
where lower(SUBSTRING(CITY, 1, 1)) not in ('a','e','i','o','u');