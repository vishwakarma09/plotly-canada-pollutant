SELECT b.year,  
b.average as `PM2,5 - BAM hr - A`, 
c.average as `O3 hr - A`, 
d.average as `NOx hr - A`,
-- other 4 months
f.average as `PM2,5 - BAM hr - B`, 
g.average as `O3 hr - B`, 
h.average as `NOx hr - B`

from
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM dump80 
where Label = 'NOX' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) b
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM dump80 
where Label = 'PM2.5' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) c 
on b.year = c.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM dump80 
where Label = 'O3' 
and month(timestamp) in (5,6,7,8)
group by year(timestamp)
) d
on b.year = d.year

-- other months

left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM dump80 
where Label = 'NOX' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) f
on b.year = f.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM dump80 
where Label = 'PM2.5' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
group by year(timestamp)
) g
on b.year = g.year
left join 
(
SELECT 
year(timestamp) as year,
Label,
EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average 
FROM dump80 
where Label = 'O3' 
and month(timestamp) in (1,2,3,4,9,10,11,12)
) h
on b.year = h.year