-- select distinct(CITY) from STATION
-- where lower(CITY) not regexp ('[^aeiou]') or lower(CITY) not regexp ('[aeiou]&');


select distinct(CITY) from STATION
where lower(left(CITY, 1)) not in ('a','e','i','o','u')
or lower(right(CITY, 1)) not in ('a','e','i','o','u');