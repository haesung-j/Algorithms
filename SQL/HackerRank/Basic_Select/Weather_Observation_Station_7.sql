-- select distinct(CITY) from STATION
-- where lower(SUBSTRING(CITY, length(CITY), length(CITY))) in ('a','e','i','o','u');

select distinct(CITY) from STATION
where CITY regexp ('[aeiou]$');