SELECT a.year,  
a.average as `CO - A`, 
-- other 4 months
a.average as `CO - B`
from
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM montreal_city 
where month(timestamp) in (5,6,7,8)
group by year(timestamp)
) a
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM montreal_city
where month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) b
on a.year = b.year