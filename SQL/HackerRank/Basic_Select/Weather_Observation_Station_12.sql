select distinct(CITY) from STATION
where lower(left(CITY, 1)) not in ('a','e','i','o','u')
and lower(right(CITY, 1)) not in ('a','e','i','o','u');